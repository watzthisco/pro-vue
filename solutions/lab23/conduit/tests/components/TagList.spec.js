import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import TagList from '@/components/TagList.vue'

describe('TagList', () => {
  it('shows the "Popular Tags" heading', () => {
    const wrapper = mount(TagList)

    expect(wrapper.find('p').text()).toBe('Popular Tags')
  })

  it('shows fallback text when no tags are slotted in', () => {
    // The <slot> has default content that is displayed when the parent passes nothing.
    const wrapper = mount(TagList)

    expect(wrapper.find('ul').text()).toBe('No tags available.')
  })

  it('renders slotted content inside the <ul> instead of the fallback text', () => {
    const wrapper = mount(TagList, { slots: { default: '<li>vue</li><li>pinia</li>' } })

    const items = wrapper.findAll('ul li')
    expect(items.map((li) => li.text())).toEqual(['vue', 'pinia'])
    expect(wrapper.text()).not.toContain('No tags available.')
  })
})
