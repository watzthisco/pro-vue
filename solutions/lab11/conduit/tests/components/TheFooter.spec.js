import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import TheFooter from '@/components/TheFooter.vue'
const createWrapper = () => mount(TheFooter)
describe('TheFooter', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper()

    expect(wrapper.exists()).toBe(true)
  })
})
