import { describe, expect, it } from 'vitest'
import { shallowMount } from '@vue/test-utils'
import { RouterView } from 'vue-router'
import App from '@/App.vue'
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'

// shallowMount stubs the children, so this test only checks how App arranges the page shell.
describe('App', () => {
  const createWrapper = () => shallowMount(App)

  it('renders the root #app container', () => {
    expect(createWrapper().find('#app').exists()).toBe(true)
  })

  it('contains the header, the routed page and the footer', () => {
    const wrapper = createWrapper()

    expect(wrapper.findComponent(TheHeader).exists()).toBe(true)
    expect(wrapper.findComponent(RouterView).exists()).toBe(true)
    expect(wrapper.findComponent(TheFooter).exists()).toBe(true)
  })

  it('orders them header -> page -> footer', () => {
    const children = createWrapper().find('#app').element.children
    const tags = Array.from(children).map((el) => el.tagName.toLowerCase())

    // Stubs are rendered as <the-header-stub>, <router-view-stub>, <the-footer-stub>.
    expect(tags).toEqual(['the-header-stub', 'router-view-stub', 'the-footer-stub'])
  })
})
