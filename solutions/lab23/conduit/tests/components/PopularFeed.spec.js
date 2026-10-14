import { describe, expect, it } from 'vitest'
import { shallowMount } from '@vue/test-utils'
import PopularFeed from '@/components/PopularFeed.vue'
import ArticleList from '@/components/ArticleList.vue'

// ArticleList is stubbed by shallowMount; we verify only the props PopularFeed supplies.
describe('PopularFeed', () => {
  it('wraps the list in a .home-popular container', () => {
    expect(shallowMount(PopularFeed).find('.home-popular').exists()).toBe(true)
  })

  it('sorts the list by favoritesCount (most favorited first)', () => {
    const list = shallowMount(PopularFeed).findComponent(ArticleList)

    expect(list.props('sortBy')).toBe('favoritesCount')
  })

  it('passes the selected tag down to the list', () => {
    const wrapper = shallowMount(PopularFeed, { props: { tag: 'sushi' } })

    expect(wrapper.findComponent(ArticleList).props('tag')).toBe('sushi')
  })

  it('defaults the tag to an empty string (no tag filter)', () => {
    expect(shallowMount(PopularFeed).findComponent(ArticleList).props('tag')).toBe('')
  })
})
