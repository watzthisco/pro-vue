import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import TheFooter from '@/components/TheFooter.vue'

const createWrapper = () => mount(TheFooter)

describe('TheFooter', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper()

    expect(wrapper.exists()).toBe(true)
  })

  it('renders a <footer> element', () => {
    expect(createWrapper().element.tagName).toBe('FOOTER')
  })

  it('shows the site name', () => {
    expect(createWrapper().text()).toContain('conduit')
  })

  it('shows the MIT license attribution', () => {
    // `&amp;` in the template should be rendered as a real ampersand.
    expect(createWrapper().find('.attribution').text()).toBe('Code & design licensed under MIT.')
  })
})
