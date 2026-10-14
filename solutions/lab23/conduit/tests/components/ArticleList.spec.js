import { beforeEach, describe, expect, it, vi } from 'vitest'
import { flushPromises, mount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import { ArticlesService } from '@/common/api.service'
import ArticleList from '@/components/ArticleList.vue'
import ArticlePreview from '@/components/ArticlePreview.vue'

// Mock only the HTTP layer. The real Pinia home store and the real ArticlePreview are used,
// which makes these tests closer to how the list behaves in the running app.
vi.mock('@/common/api.service', () => ({
  ArticlesService: { query: vi.fn() },
}))

const articles = [
  { slug: 'a', title: 'Alpha', description: 'first', tagList: ['vue'], favoritesCount: 1 },
  { slug: 'b', title: 'Beta', description: 'second', tagList: ['pinia'], favoritesCount: 9 },
  { slug: 'c', title: 'Gamma', description: 'third', tagList: ['vue', 'pinia'], favoritesCount: 5 },
]

let pinia

beforeEach(() => {
  vi.clearAllMocks()
  pinia = createPinia()
  setActivePinia(pinia)
  ArticlesService.query.mockResolvedValue({
    data: { articles, articlesCount: articles.length },
  })
})

// Mounts the list and (by default) waits for the on-mount fetch to finish.
async function createWrapper(props = {}, { settle = true } = {}) {
  const wrapper = mount(ArticleList, { props, global: { plugins: [pinia] } })
  if (settle) await flushPromises()
  return wrapper
}

const titles = (wrapper) =>
  wrapper.findAllComponents(ArticlePreview).map((p) => p.props('article').title)

describe('ArticleList', () => {
  describe('loading and fetching', () => {
    it('shows a loading message until the articles have arrived', async () => {
      const wrapper = await createWrapper({}, { settle: false })

      expect(wrapper.text()).toContain('Loading articles...')

      await flushPromises()

      expect(wrapper.text()).not.toContain('Loading articles...')
    })

    it('requests all articles when mounted', async () => {
      await createWrapper()

      expect(ArticlesService.query).toHaveBeenCalledTimes(1)
      expect(ArticlesService.query).toHaveBeenCalledWith('all', undefined)
    })

    it('renders one ArticlePreview per article', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.findAllComponents(ArticlePreview)).toHaveLength(3)
      expect(titles(wrapper)).toEqual(['Alpha', 'Beta', 'Gamma'])
    })

    it('shows an empty-state message when there are no articles', async () => {
      ArticlesService.query.mockResolvedValue({ data: { articles: [], articlesCount: 0 } })

      const wrapper = await createWrapper()

      expect(wrapper.text()).toContain('No articles are here... yet.')
      expect(wrapper.findAllComponents(ArticlePreview)).toHaveLength(0)
    })

    it('does not show the empty-state message when there are articles', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.text()).not.toContain('No articles are here... yet.')
    })
  })

  describe('tag slot', () => {
    it("renders each article's tags inside its preview", async () => {
      const wrapper = await createWrapper()

      const gammaTags = wrapper
        .findAllComponents(ArticlePreview)[2]
        .findAll('.tag-list li')
        .map((li) => li.text())
      expect(gammaTags).toEqual(['vue', 'pinia'])
    })
  })

  describe('text search', () => {
    it('shows a filter input', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.find('input[placeholder="filter articles"]').exists()).toBe(true)
    })

    it('narrows the list to articles whose title matches the typed text', async () => {
      const wrapper = await createWrapper()

      await wrapper.find('input').setValue('beta')

      expect(titles(wrapper)).toEqual(['Beta'])
    })

    it('also matches against the description', async () => {
      const wrapper = await createWrapper()

      await wrapper.find('input').setValue('third')

      expect(titles(wrapper)).toEqual(['Gamma'])
    })

    it('shows every article again once the input is cleared', async () => {
      const wrapper = await createWrapper()
      const input = wrapper.find('input')

      await input.setValue('beta')
      await input.setValue('')

      expect(titles(wrapper)).toHaveLength(3)
    })
  })

  describe('tag prop', () => {
    it('only shows articles that include the selected tag', async () => {
      const wrapper = await createWrapper({ tag: 'pinia' })

      expect(titles(wrapper)).toEqual(['Beta', 'Gamma'])
    })

    it('shows everything when the tag is empty', async () => {
      const wrapper = await createWrapper({ tag: '' })

      expect(titles(wrapper)).toHaveLength(3)
    })

    it('reacts when the tag prop changes', async () => {
      const wrapper = await createWrapper({ tag: 'vue' })
      expect(titles(wrapper)).toEqual(['Alpha', 'Gamma'])

      await wrapper.setProps({ tag: 'pinia' })

      expect(titles(wrapper)).toEqual(['Beta', 'Gamma'])
    })

    it('combines with the text search (both must match)', async () => {
      const wrapper = await createWrapper({ tag: 'vue' })

      await wrapper.find('input').setValue('gamma')

      expect(titles(wrapper)).toEqual(['Gamma'])
    })

    it('treats articles without a tagList as having no tags instead of crashing', async () => {
      ArticlesService.query.mockResolvedValue({
        data: { articles: [{ slug: 'x', title: 'No tags', description: '' }], articlesCount: 1 },
      })

      const wrapper = await createWrapper({ tag: 'vue' })

      expect(titles(wrapper)).toEqual([])
    })
  })

  describe('sortBy prop', () => {
    it('keeps API order when no sort is requested', async () => {
      const wrapper = await createWrapper()

      expect(titles(wrapper)).toEqual(['Alpha', 'Beta', 'Gamma'])
    })

    it('sorts by the given numeric field, highest first', async () => {
      const wrapper = await createWrapper({ sortBy: 'favoritesCount' })

      expect(titles(wrapper)).toEqual(['Beta', 'Gamma', 'Alpha'])
    })

    it('sorts a copy, leaving the order in the store unchanged', async () => {
      const wrapper = await createWrapper({ sortBy: 'favoritesCount' })
      const { useHomeStore } = await import('@/stores/home')

      expect(titles(wrapper)[0]).toBe('Beta')
      expect(useHomeStore().articles.map((a) => a.slug)).toEqual(['a', 'b', 'c'])
    })
  })

  describe('font size controls', () => {
    const fontSizeOf = (wrapper, index = 0) =>
      wrapper.findAllComponents(ArticlePreview)[index].element.style.fontSize

    const click = (wrapper, label, index = 0) =>
      wrapper
        .findAllComponents(ArticlePreview)
        [index].findAll('button')
        .find((b) => b.text() === label)
        .trigger('click')

    it('starts at 1em', async () => {
      expect(fontSizeOf(await createWrapper())).toBe('1em')
    })

    it('grows by 0.1em when a preview emits "enlarge-text"', async () => {
      const wrapper = await createWrapper()

      await click(wrapper, 'Enlarge Text')

      expect(fontSizeOf(wrapper)).toBe('1.1em')
    })

    it('shrinks by 0.1em when a preview emits "shrink-text"', async () => {
      const wrapper = await createWrapper()

      await click(wrapper, 'Shrink Text')

      expect(fontSizeOf(wrapper)).toBe('0.9em')
    })

    it('applies the size to every preview, since the size state lives in the list', async () => {
      const wrapper = await createWrapper()

      await click(wrapper, 'Enlarge Text', 1)

      expect(fontSizeOf(wrapper, 0)).toBe('1.1em')
      expect(fontSizeOf(wrapper, 2)).toBe('1.1em')
    })
  })
})
