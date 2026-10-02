import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import { createPinia } from 'pinia'
import TheHeader from '@/components/TheHeader.vue'
const createWrapper = () =>
  mount(TheHeader, { global: { plugins: [createPinia()], stubs: ['RouterLink'] } })
describe('TheHeader', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper()

    expect(wrapper.exists()).toBe(true)
  })
})
