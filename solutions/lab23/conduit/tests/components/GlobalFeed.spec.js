import { describe, expect, it } from 'vitest'
import { shallowMount } from '@vue/test-utils'
import GlobalFeed from '@/components/GlobalFeed.vue'
import ArticleList from '@/components/ArticleList.vue'

// shallowMount replaces ArticleList with a stub, so we only test what GlobalFeed itself does:
// wiring the right props into the list.
describe('GlobalFeed', () => {
  it('wraps the list in a .home-global container', () => {
    expect(shallowMount(GlobalFeed).find('.home-global').exists()).toBe(true)
  })

  it('renders an ArticleList for "all" articles', () => {
    const list = shallowMount(GlobalFeed).findComponent(ArticleList)

    expect(list.exists()).toBe(true)
    expect(list.attributes('type')).toBe('all')
  })

  it('does not set a sort order (articles are shown in API order)', () => {
    const list = shallowMount(GlobalFeed).findComponent(ArticleList)

    expect(list.props('sortBy')).toBe('')
  })

  it('passes the selected tag down to the list', () => {
    const wrapper = shallowMount(GlobalFeed, { props: { tag: 'vue' } })

    expect(wrapper.findComponent(ArticleList).props('tag')).toBe('vue')
  })

  it('defaults the tag to an empty string (no tag filter)', () => {
    expect(shallowMount(GlobalFeed).findComponent(ArticleList).props('tag')).toBe('')
  })
})
