import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import ArticlePreview from '@/components/ArticlePreview.vue'

const article = {
  title: 'How to train a dragon',
  description: 'A short guide',
  slug: 'how-to-train-a-dragon',
}

const createWrapper = (options = {}) => mount(ArticlePreview, { props: { article }, ...options })

// The component has three buttons; these helpers find them by their visible label / class.
const findButton = (wrapper, text) => wrapper.findAll('button').find((b) => b.text().includes(text))
const findFavoriteButton = (wrapper) => wrapper.find('button.btn-sm')

describe('ArticlePreview', () => {
  describe('rendering', () => {
    it('shows the article title and description', () => {
      const wrapper = createWrapper()

      expect(wrapper.find('h1').text()).toBe(article.title)
      expect(wrapper.find('p').text()).toBe(article.description)
    })

    it('links to the article page using the slug', () => {
      const link = createWrapper().find('a')

      expect(link.text()).toBe('Read more...')
      expect(link.attributes('href')).toBe('/article/how-to-train-a-dragon')
    })

    it('renders content passed to the "tags" slot', () => {
      const wrapper = createWrapper({
        slots: { tags: '<ul class="tag-list"><li>dragons</li></ul>' },
      })

      expect(wrapper.find('.tag-list li').text()).toBe('dragons')
    })

    it('renders nothing extra when the "tags" slot is not provided', () => {
      expect(createWrapper().find('.tag-list').exists()).toBe(false)
    })

    it('requires the article prop', () => {
      // Vue warns (but does not throw) for missing required props, so we assert on the
      // component definition instead of on a runtime error.
      expect(ArticlePreview.props.article.required).toBe(true)
    })
  })

  describe('favorite button', () => {
    it('starts un-favorited: outline style and a count of 0', () => {
      const button = findFavoriteButton(createWrapper())

      expect(button.classes()).toContain('btn-outline-primary')
      expect(button.classes()).not.toContain('btn-primary')
      expect(button.text()).toBe('0')
    })

    it('switches to the filled style and increments the count after a click', async () => {
      const wrapper = createWrapper()
      const button = findFavoriteButton(wrapper)

      await button.trigger('click')

      expect(button.classes()).toContain('btn-primary')
      expect(button.classes()).not.toContain('btn-outline-primary')
      expect(button.text()).toBe('1')
    })

    it('goes back to the outline style on a second click', async () => {
      const wrapper = createWrapper()
      const button = findFavoriteButton(wrapper)

      await button.trigger('click')
      await button.trigger('click')

      expect(button.classes()).toContain('btn-outline-primary')
      expect(button.classes()).not.toContain('btn-primary')
    })

    it('keeps the state of each preview independent', async () => {
      // Each instance owns its own refs, so favoriting one article must not affect another.
      const first = createWrapper()
      const second = createWrapper()

      await findFavoriteButton(first).trigger('click')

      expect(findFavoriteButton(first).text()).toBe('1')
      expect(findFavoriteButton(second).text()).toBe('0')
    })
  })

  describe('text size events', () => {
    it('emits "enlarge-text" with 0.1 when "Enlarge Text" is clicked', async () => {
      const wrapper = createWrapper()

      await findButton(wrapper, 'Enlarge Text').trigger('click')

      expect(wrapper.emitted('enlarge-text')).toEqual([[0.1]])
      expect(wrapper.emitted('shrink-text')).toBeUndefined()
    })

    it('emits "shrink-text" with 0.1 when "Shrink Text" is clicked', async () => {
      const wrapper = createWrapper()

      await findButton(wrapper, 'Shrink Text').trigger('click')

      expect(wrapper.emitted('shrink-text')).toEqual([[0.1]])
      expect(wrapper.emitted('enlarge-text')).toBeUndefined()
    })
  })
})
