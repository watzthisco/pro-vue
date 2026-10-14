import { beforeEach, describe, expect, it, vi } from 'vitest'
import { createPinia, setActivePinia } from 'pinia'
import { ArticlesService } from '@/common/api.service'
import { useHomeStore } from '@/stores/home'

// Replace the HTTP layer so the store is tested in isolation.
vi.mock('@/common/api.service', () => ({
  ArticlesService: { query: vi.fn() },
}))

beforeEach(() => {
  vi.clearAllMocks()
  // A fresh pinia per test gives every test a brand new store instance.
  setActivePinia(createPinia())
})

describe('home store', () => {
  describe('initial state', () => {
    it('starts empty and in the loading state', () => {
      const store = useHomeStore()

      expect(store.tags).toEqual([])
      expect(store.articles).toEqual([])
      expect(store.articlesCount).toBe(0)
      // isLoading starts true so the UI shows "Loading articles..." before the first fetch.
      expect(store.isLoading).toBe(true)
    })
  })

  describe('fetchArticles', () => {
    it('stores the articles and count returned by the API', async () => {
      ArticlesService.query.mockResolvedValue({
        data: { articles: [{ slug: 'a' }, { slug: 'b' }], articlesCount: 2 },
      })
      const store = useHomeStore()

      await store.fetchArticles({ type: 'all' })

      expect(store.articles).toEqual([{ slug: 'a' }, { slug: 'b' }])
      expect(store.articlesCount).toBe(2)
    })

    it('forwards the type and filters to ArticlesService.query', async () => {
      ArticlesService.query.mockResolvedValue({ data: { articles: [], articlesCount: 0 } })
      const store = useHomeStore()

      await store.fetchArticles({ type: 'feed', filters: { limit: 10 } })

      expect(ArticlesService.query).toHaveBeenCalledWith('feed', { limit: 10 })
    })

    it('works when called with no arguments (default params)', async () => {
      ArticlesService.query.mockResolvedValue({ data: { articles: [], articlesCount: 0 } })

      await useHomeStore().fetchArticles()

      expect(ArticlesService.query).toHaveBeenCalledWith(undefined, undefined)
    })

    it('is loading while the request is in flight and done afterwards', async () => {
      // Hold the request open with a promise we resolve manually.
      let resolveRequest
      ArticlesService.query.mockReturnValue(
        new Promise((resolve) => {
          resolveRequest = resolve
        }),
      )
      const store = useHomeStore()
      store.isLoading = false

      const pending = store.fetchArticles({ type: 'all' })
      expect(store.isLoading).toBe(true)

      resolveRequest({ data: { articles: [], articlesCount: 0 } })
      await pending

      expect(store.isLoading).toBe(false)
    })

    it('stops loading and re-throws when the request fails', async () => {
      ArticlesService.query.mockRejectedValue(new Error('network down'))
      const store = useHomeStore()

      await expect(store.fetchArticles({ type: 'all' })).rejects.toThrow('network down')

      // The `finally` block must clear the spinner even on failure.
      expect(store.isLoading).toBe(false)
    })

    it('keeps the previous articles when a request fails', async () => {
      const store = useHomeStore()
      store.articles = [{ slug: 'existing' }]
      ArticlesService.query.mockRejectedValue(new Error('nope'))

      await expect(store.fetchArticles()).rejects.toThrow('nope')

      expect(store.articles).toEqual([{ slug: 'existing' }])
    })
  })

  describe('setTags', () => {
    it('replaces the tag list', () => {
      const store = useHomeStore()

      store.setTags(['vue', 'pinia'])
      expect(store.tags).toEqual(['vue', 'pinia'])

      store.setTags(['router'])
      expect(store.tags).toEqual(['router'])
    })
  })

  describe('updateArticleInList', () => {
    it('updates favorited and favoritesCount of the matching article only', () => {
      const store = useHomeStore()
      store.articles = [
        { slug: 'a', title: 'A', favorited: false, favoritesCount: 0 },
        { slug: 'b', title: 'B', favorited: false, favoritesCount: 5 },
      ]

      store.updateArticleInList({ slug: 'a', favorited: true, favoritesCount: 1 })

      expect(store.articles[0]).toEqual({
        slug: 'a',
        title: 'A',
        favorited: true,
        favoritesCount: 1,
      })
      // The other article must be left untouched.
      expect(store.articles[1]).toEqual({
        slug: 'b',
        title: 'B',
        favorited: false,
        favoritesCount: 5,
      })
    })

    it('preserves the other properties of the updated article', () => {
      const store = useHomeStore()
      store.articles = [{ slug: 'a', title: 'Keep me', body: 'Keep me too', favoritesCount: 0 }]

      store.updateArticleInList({ slug: 'a', favorited: true, favoritesCount: 3 })

      expect(store.articles[0].title).toBe('Keep me')
      expect(store.articles[0].body).toBe('Keep me too')
    })

    it('does nothing when no article has the given slug', () => {
      const store = useHomeStore()
      store.articles = [{ slug: 'a', favorited: false, favoritesCount: 0 }]

      store.updateArticleInList({ slug: 'missing', favorited: true, favoritesCount: 9 })

      expect(store.articles).toEqual([{ slug: 'a', favorited: false, favoritesCount: 0 }])
    })

    it('replaces the array (new reference) so Vue reactivity picks up the change', () => {
      const store = useHomeStore()
      store.articles = [{ slug: 'a', favorited: false, favoritesCount: 0 }]
      const before = store.articles

      store.updateArticleInList({ slug: 'a', favorited: true, favoritesCount: 1 })

      expect(store.articles).not.toBe(before)
    })
  })
})
