import { beforeEach, describe, expect, it, vi } from 'vitest'
import { flushPromises, mount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import { createMemoryHistory, createRouter } from 'vue-router'
import TheHeader from '@/components/TheHeader.vue'
import { useAuthStore } from '@/stores/auth'

// The auth store imports the API service; mock it so no real HTTP client is created.
vi.mock('@/common/api.service', () => ({ default: { post: vi.fn(), get: vi.fn(), put: vi.fn() } }))

const stub = { template: '<div />' }

let router
let pinia

beforeEach(async () => {
  window.localStorage.clear()
  pinia = createPinia()
  setActivePinia(pinia)
  // A real (in-memory) router lets us assert on actual navigation and active-link classes.
  router = createRouter({
    history: createMemoryHistory(),
    routes: [
      { name: 'home', path: '/', component: stub },
      { name: 'login', path: '/login', component: stub },
      { name: 'register', path: '/register', component: stub },
    ],
  })
  await router.push('/')
  await router.isReady()
})

const createWrapper = () => mount(TheHeader, { global: { plugins: [pinia, router] } })
const linkTexts = (wrapper) => wrapper.findAll('a').map((a) => a.text())

describe('TheHeader', () => {
  it('should render without a problem', () => {
    expect(createWrapper().exists()).toBe(true)
  })

  it('shows the brand link pointing home', () => {
    const brand = createWrapper().find('a.navbar-brand')

    expect(brand.text()).toBe('Conduit')
    expect(brand.attributes('href')).toBe('/')
  })

  describe('when logged out', () => {
    it('shows Home, Sign In and Sign Up links', () => {
      expect(linkTexts(createWrapper())).toEqual(['Conduit', 'Home', 'Sign In', 'Sign Up'])
    })

    it('does not show the Log out link', () => {
      expect(linkTexts(createWrapper())).not.toContain('Log out')
    })

    it('links to the login and register routes', () => {
      const wrapper = createWrapper()
      const href = (label) =>
        wrapper
          .findAll('a')
          .find((a) => a.text() === label)
          .attributes('href')

      expect(href('Sign In')).toBe('/login')
      expect(href('Sign Up')).toBe('/register')
    })
  })

  describe('when logged in', () => {
    beforeEach(() => {
      useAuthStore().isAuthenticated = true
    })

    it('shows Home and Log out only', () => {
      expect(linkTexts(createWrapper())).toEqual(['Conduit', 'Home', 'Log out'])
    })

    it('hides the Sign In and Sign Up links', () => {
      const texts = linkTexts(createWrapper())

      expect(texts).not.toContain('Sign In')
      expect(texts).not.toContain('Sign Up')
    })

    it('logs out and returns to the home page when "Log out" is clicked', async () => {
      const store = useAuthStore()
      store.setAuth({ username: 'jane', token: 'tok' })
      await router.push('/login')
      const wrapper = createWrapper()
      const logoutSpy = vi.spyOn(store, 'logout')

      await wrapper
        .findAll('a')
        .find((a) => a.text() === 'Log out')
        .trigger('click')
      await flushPromises()

      expect(logoutSpy).toHaveBeenCalledTimes(1)
      expect(store.isAuthenticated).toBe(false)
      expect(window.localStorage.getItem('id_token')).toBeNull()
      expect(router.currentRoute.value.name).toBe('home')
    })

    it('switches the nav back to the logged-out links after logging out', async () => {
      const store = useAuthStore()
      store.setAuth({ token: 'tok' })
      const wrapper = createWrapper()

      await wrapper
        .findAll('a')
        .find((a) => a.text() === 'Log out')
        .trigger('click')
      await flushPromises()

      expect(linkTexts(wrapper)).toContain('Sign In')
      expect(linkTexts(wrapper)).not.toContain('Log out')
    })
  })

  describe('active link highlighting', () => {
    it('marks Home active on the home route', () => {
      const home = createWrapper()
        .findAll('a')
        .find((a) => a.text() === 'Home')

      expect(home.classes()).toContain('active')
    })

    it('marks Sign In active on the login route and un-marks Home', async () => {
      await router.push('/login')
      const wrapper = createWrapper()
      const byText = (label) => wrapper.findAll('a').find((a) => a.text() === label)

      expect(byText('Sign In').classes()).toContain('active')
      expect(byText('Home').classes()).not.toContain('active')
    })
  })
})
