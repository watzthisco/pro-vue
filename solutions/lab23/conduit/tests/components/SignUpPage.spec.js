import { beforeEach, describe, expect, it, vi } from 'vitest'
import { flushPromises, mount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import { createMemoryHistory, createRouter } from 'vue-router'
import ApiService from '@/common/api.service'
import SignUpPage from '@/components/SignUpPage.vue'
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
      { name: 'login', path: '/login', component: stub },
      { name: 'register', path: '/register', component: SignUpPage },
    ],
  })
  await router.push('/register')
  await router.isReady()
})

const createWrapper = () => mount(SignUpPage, { global: { plugins: [pinia, router] } })

// Fills in and submits the form the way a user would.
async function submitForm(wrapper, values = {}) {
  const { username = 'jane', email = 'jane@example.com', password = 'secret' } = values
  await wrapper.find('input[placeholder="Username"]').setValue(username)
  await wrapper.find('input[placeholder="Email"]').setValue(email)
  await wrapper.find('input[placeholder="Password"]').setValue(password)
  await wrapper.find('form').trigger('submit')
  await flushPromises()
}

describe('SignUpPage', () => {
  describe('rendering', () => {
    it('shows the "Sign up" heading', () => {
      expect(createWrapper().find('h1').text()).toBe('Sign up')
    })

    it('shows username, email and password inputs and a submit button', () => {
      const wrapper = createWrapper()

      expect(wrapper.find('input[placeholder="Username"]').exists()).toBe(true)
      expect(wrapper.find('input[placeholder="Email"]').exists()).toBe(true)
      expect(wrapper.find('input[placeholder="Password"]').attributes('type')).toBe('password')
      expect(wrapper.find('button').text()).toBe('Sign up')
    })

    it('links to the login page', () => {
      const link = createWrapper().find('a')

      expect(link.text()).toBe('Have an account?')
      expect(link.attributes('href')).toBe('/login')
    })

    it('does not show an error list initially', () => {
      expect(createWrapper().find('.error-messages').exists()).toBe(false)
    })
  })

  describe('submitting valid details', () => {
    beforeEach(() => {
      ApiService.post.mockResolvedValue({
        data: { user: { username: 'jane', email: 'jane@example.com', token: 'tok' } },
      })
    })

    it('sends the typed username, email and password to the users endpoint', async () => {
      await submitForm(createWrapper())

      expect(ApiService.post).toHaveBeenCalledWith('users', {
        user: { username: 'jane', email: 'jane@example.com', password: 'secret' },
      })
    })

    it('authenticates the new user and saves the token', async () => {
      await submitForm(createWrapper())

      expect(useAuthStore().isAuthenticated).toBe(true)
      expect(window.localStorage.getItem('id_token')).toBe('tok')
    })

    it('redirects to the home page', async () => {
      await submitForm(createWrapper())

      expect(router.currentRoute.value.name).toBe('home')
    })
  })

  describe('submitting invalid details', () => {
    beforeEach(() => {
      ApiService.post.mockRejectedValue({
        response: { data: { errors: { email: ['has already been taken'] } } },
      })
    })

    it('shows the API error messages', async () => {
      const wrapper = createWrapper()

      await submitForm(wrapper)

      expect(wrapper.find('.error-messages li').text()).toBe('email has already been taken')
    })

    it('stays on the sign-up page', async () => {
      await submitForm(createWrapper())

      expect(router.currentRoute.value.name).toBe('register')
    })

    it('does not authenticate the user or store a token', async () => {
      await submitForm(createWrapper())

      expect(useAuthStore().isAuthenticated).toBe(false)
      expect(window.localStorage.getItem('id_token')).toBeNull()
    })

    it('does not let the rejection escape the submit handler', async () => {
      await expect(submitForm(createWrapper())).resolves.toBeUndefined()
    })
  })

  describe('error formatting', () => {
    it('joins multiple messages for one field and lists each failing field', async () => {
      ApiService.post.mockRejectedValue({
        response: {
          data: {
            errors: { username: ['is required', 'is too short'], password: ['is required'] },
          },
        },
      })
      const wrapper = createWrapper()

      await submitForm(wrapper)

      const items = wrapper.findAll('.error-messages li').map((li) => li.text())
      expect(items).toEqual(['username is required, is too short', 'password is required'])
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
