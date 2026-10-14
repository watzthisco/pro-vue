import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import TagItem from '@/components/TagItem.vue'

const createWrapper = (props = {}) => mount(TagItem, { props: { tag: 'vue', ...props } })

describe('TagItem', () => {
  it('renders the tag text', () => {
    const wrapper = createWrapper({ tag: 'dragons' })

    expect(wrapper.text()).toBe('dragons')
  })

  it('is not highlighted by default', () => {
    // `active` is optional and defaults to false.
    expect(createWrapper().classes()).not.toContain('active')
  })

  it('gets the "active" class when the active prop is true', () => {
    expect(createWrapper({ active: true }).classes()).toContain('active')
  })

  it('always has the base tag styling classes', () => {
    expect(createWrapper().classes()).toEqual(
      expect.arrayContaining(['tag-default', 'tag-pill', 'tag-outline']),
    )
  })

  it('emits "select" with the tag name when clicked', async () => {
    const wrapper = createWrapper({ tag: 'sushi' })

    await wrapper.trigger('click')

    // The parent uses this payload to know *which* tag was chosen.
    expect(wrapper.emitted('select')).toEqual([['sushi']])
  })

  it('emits one "select" event per click', async () => {
    const wrapper = createWrapper()

    await wrapper.trigger('click')
    await wrapper.trigger('click')

    expect(wrapper.emitted('select')).toHaveLength(2)
  })
})
