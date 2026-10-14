import { beforeEach, describe, expect, it, vi } from 'vitest'
import { flushPromises, mount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import { createMemoryHistory, createRouter } from 'vue-router'
import ApiService from '@/common/api.service'
import LoginPage from '@/components/LoginPage.vue'
import { useAuthStore } from '@/stores/auth'

// Mock the HTTP layer; the real auth store and router are used so the whole
// "submit form -> call API -> update store -> navigate" flow is exercised.
vi.mock('@/common/api.service', () => ({
  default: { post: vi.fn(), get: vi.fn(), put: vi.fn(), setHeader: vi.fn() },
}))

const stub = { template: '<div />' }

let pinia
let router

beforeEach(async () => {
  window.localStorage.clear()
  vi.clearAllMocks()
  pinia = createPinia()
  setActivePinia(pinia)
  router = createRouter({
    history: createMemoryHistory(),
    routes: [
      { name: 'home', path: '/', component: stub },
      { name: 'login', path: '/login', component: LoginPage },
      { name: 'register', path: '/register', component: stub },
    ],
  })
  await router.push('/login')
  await router.isReady()
})

const createWrapper = () => mount(LoginPage, { global: { plugins: [pinia, router] } })

// Fills in and submits the form the way a user would.
async function submitForm(wrapper, email = 'jane@example.com', password = 'secret') {
  await wrapper.find('input[type="text"]').setValue(email)
  await wrapper.find('input[type="password"]').setValue(password)
  await wrapper.find('form').trigger('submit')
  await flushPromises()
}

describe('LoginPage', () => {
  describe('rendering', () => {
    it('shows the "Sign in" heading', () => {
      expect(createWrapper().find('h1').text()).toBe('Sign in')
    })

    it('shows email and password inputs and a submit button', () => {
      const wrapper = createWrapper()

      expect(wrapper.find('input[placeholder="Email"]').exists()).toBe(true)
      expect(wrapper.find('input[placeholder="Password"]').attributes('type')).toBe('password')
      expect(wrapper.find('button').text()).toBe('Sign in')
    })

    it('links to the registration page', () => {
      const link = createWrapper().find('a')

      expect(link.text()).toBe('Need an account?')
      expect(link.attributes('href')).toBe('/register')
    })

    it('does not show an error list initially', () => {
      expect(createWrapper().find('.error-messages').exists()).toBe(false)
    })
  })

  describe('submitting valid credentials', () => {
    beforeEach(() => {
      ApiService.post.mockResolvedValue({
        data: { user: { email: 'jane@example.com', username: 'jane', token: 'tok' } },
      })
    })

    it('sends the typed email and password to the login endpoint', async () => {
      const wrapper = createWrapper()

      await submitForm(wrapper)

      expect(ApiService.post).toHaveBeenCalledWith('users/login', {
        user: { email: 'jane@example.com', password: 'secret' },
      })
    })

    it('authenticates the user in the store', async () => {
      await submitForm(createWrapper())

      expect(useAuthStore().isAuthenticated).toBe(true)
      expect(useAuthStore().user.username).toBe('jane')
    })

    it('redirects to the home page', async () => {
      await submitForm(createWrapper())

      expect(router.currentRoute.value.name).toBe('home')
    })
  })

  describe('submitting invalid credentials', () => {
    beforeEach(() => {
      ApiService.post.mockRejectedValue({
        response: { data: { errors: { 'email or password': ['is invalid'] } } },
      })
    })

    it('shows the API error messages', async () => {
      const wrapper = createWrapper()

      await submitForm(wrapper)

      // Each error renders as "<field> <message>".
      expect(wrapper.find('.error-messages li').text()).toBe('email or password is invalid')
    })

    it('stays on the login page', async () => {
      await submitForm(createWrapper())

      expect(router.currentRoute.value.name).toBe('login')
    })

    it('does not authenticate the user', async () => {
      await submitForm(createWrapper())

      expect(useAuthStore().isAuthenticated).toBe(false)
    })

    it('does not let the rejection escape the submit handler', async () => {
      // If the page forgot its try/catch we would get an unhandled rejection that fails the run.
      await expect(submitForm(createWrapper())).resolves.toBeUndefined()
    })
  })

  describe('error formatting', () => {
    it('joins multiple messages for one field with a comma', async () => {
      ApiService.post.mockRejectedValue({
        response: { data: { errors: { email: ['is required', 'is invalid'] } } },
      })
      const wrapper = createWrapper()

      await submitForm(wrapper)

      expect(wrapper.find('.error-messages li').text()).toBe('email is required, is invalid')
    })

    it('renders one list item per failing field', async () => {
      ApiService.post.mockRejectedValue({
        response: { data: { errors: { email: ['is required'], password: ['is required'] } } },
      })
      const wrapper = createWrapper()

      await submitForm(wrapper)

      expect(wrapper.findAll('.error-messages li')).toHaveLength(2)
    })

    it('supports a plain string message (non-array)', async () => {
      ApiService.post.mockRejectedValue({ response: { data: { errors: { email: 'is bad' } } } })
      const wrapper = createWrapper()

      await submitForm(wrapper)

      expect(wrapper.find('.error-messages li').text()).toBe('email is bad')
    })

    it('shows a generic error when the server cannot be reached', async () => {
      ApiService.post.mockRejectedValue(new Error('Network Error'))
      const wrapper = createWrapper()

      await submitForm(wrapper)

      expect(wrapper.find('.error-messages li').text()).toBe('error Network Error')
    })
  })
})
