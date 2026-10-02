import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import HomeContent from '@/components/HomeContent.vue'
const createWrapper = () => mount(HomeContent)
describe('HomeContent', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper()

    expect(wrapper.exists()).toBe(true)
  })
})
