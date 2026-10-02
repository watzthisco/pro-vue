import { beforeEach, describe, expect, it, vi } from 'vitest'
import { shallowMount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import HomeContent from '@/components/HomeContent.vue'

// HomeContent requests /tags on mount, so keep the test off the network.
vi.mock('@/common/api.service', () => ({
  default: { query: vi.fn().mockResolvedValue({ data: { tags: [] } }) },
}))

const router = createRouter({
  history: createWebHistory(),
  routes: [{ name: 'home', path: '/', component: { template: '<div />' } }],
})

let pinia

beforeEach(() => {
  pinia = createPinia()
  setActivePinia(pinia)
})

const createWrapper = () => shallowMount(HomeContent, { global: { plugins: [pinia, router] } })

describe('HomeContent', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper()

    expect(wrapper.exists()).toBe(true)
  })
})
