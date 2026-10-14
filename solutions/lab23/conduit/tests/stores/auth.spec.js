import { beforeEach, describe, expect, it, vi } from 'vitest'
import { createPinia, setActivePinia } from 'pinia'
import ApiService from '@/common/api.service'
import { useAuthStore } from '@/stores/auth'

// Replace the HTTP layer so the store is tested in isolation (no network).
vi.mock('@/common/api.service', () => ({
  default: { post: vi.fn(), get: vi.fn(), put: vi.fn(), setHeader: vi.fn() },
}))

beforeEach(() => {
  // The JWT is persisted in localStorage, so clear it between tests.
  window.localStorage.clear()
  vi.clearAllMocks()
  // The store reads localStorage when it is created, so a fresh pinia must be created
  // *after* each test arranges its storage state.
  setActivePinia(createPinia())
})

describe('auth store', () => {
  describe('initial state', () => {
    it('starts unauthenticated when there is no stored token', () => {
      const store = useAuthStore()

      expect(store.isAuthenticated).toBe(false)
      expect(store.user).toEqual({})
      expect(store.errors).toBeNull()
    })

    it('starts authenticated when a token is already in localStorage', () => {
      // Simulates a returning visitor who logged in during a previous session.
      window.localStorage.setItem('id_token', 'existing-token')
      setActivePinia(createPinia())

      expect(useAuthStore().isAuthenticated).toBe(true)
    })

    it('currentUser getter returns the user state', () => {
      const store = useAuthStore()
      store.user = { username: 'jane' }

      expect(store.currentUser).toEqual({ username: 'jane' })
    })
  })

  describe('setAuth / purgeAuth', () => {
    it('setAuth marks the user authenticated, saves the token and clears errors', () => {
      const store = useAuthStore()
      store.errors = { email: ['bad'] }

      store.setAuth({ username: 'jane', token: 'tok' })

      expect(store.isAuthenticated).toBe(true)
      expect(store.user).toEqual({ username: 'jane', token: 'tok' })
      expect(store.errors).toEqual({})
      expect(window.localStorage.getItem('id_token')).toBe('tok')
    })

    it('purgeAuth resets the state and removes the token', () => {
      const store = useAuthStore()
      store.setAuth({ username: 'jane', token: 'tok' })

      store.purgeAuth()

      expect(store.isAuthenticated).toBe(false)
      expect(store.user).toEqual({})
      expect(store.errors).toEqual({})
      expect(window.localStorage.getItem('id_token')).toBeNull()
    })
  })

  describe('login', () => {
    it('stores the user and token after a successful login', async () => {
      ApiService.post.mockResolvedValue({ data: { user: { email: 'a@b.c', token: 'abc' } } })
      const store = useAuthStore()

      await store.login({ email: 'a@b.c', password: 'pw' })

      // The credentials must be wrapped in a { user } envelope, as the RealWorld API expects.
      expect(ApiService.post).toHaveBeenCalledWith('users/login', {
        user: { email: 'a@b.c', password: 'pw' },
      })
      expect(store.isAuthenticated).toBe(true)
      expect(store.user.email).toBe('a@b.c')
      expect(window.localStorage.getItem('id_token')).toBe('abc')
    })

    it('returns the response data to the caller', async () => {
      const data = { user: { token: 'abc' } }
      ApiService.post.mockResolvedValue({ data })

      await expect(useAuthStore().login({})).resolves.toBe(data)
    })

    it('records API validation errors and re-throws when login fails', async () => {
      ApiService.post.mockRejectedValue({
        response: { data: { errors: { 'email or password': ['is invalid'] } } },
      })
      const store = useAuthStore()

      await expect(store.login({ email: 'x', password: 'y' })).rejects.toBeDefined()

      expect(store.isAuthenticated).toBe(false)
      expect(store.errors).toEqual({ 'email or password': ['is invalid'] })
    })

    it('falls back to the error message when the failure has no API response (e.g. offline)', async () => {
      ApiService.post.mockRejectedValue(new Error('Network Error'))
      const store = useAuthStore()

      await expect(store.login({})).rejects.toThrow('Network Error')

      expect(store.errors).toEqual({ error: ['Network Error'] })
    })

    it('does not save a token when login fails', async () => {
      ApiService.post.mockRejectedValue(new Error('fail'))

      await expect(useAuthStore().login({})).rejects.toThrow('fail')

      expect(window.localStorage.getItem('id_token')).toBeNull()
    })
  })

  describe('logout', () => {
    it('clears the user and token on logout', async () => {
      ApiService.post.mockResolvedValue({ data: { user: { token: 'abc' } } })
      const store = useAuthStore()
      await store.login({})

      store.logout()

      expect(store.isAuthenticated).toBe(false)
      expect(window.localStorage.getItem('id_token')).toBeNull()
    })
  })

  describe('register', () => {
    it('posts to /users and logs the new user in', async () => {
      ApiService.post.mockResolvedValue({
        data: { user: { username: 'jane', email: 'j@x.y', token: 'new-token' } },
      })
      const store = useAuthStore()

      await store.register({ username: 'jane', email: 'j@x.y', password: 'pw' })

      expect(ApiService.post).toHaveBeenCalledWith('users', {
        user: { username: 'jane', email: 'j@x.y', password: 'pw' },
      })
      expect(store.isAuthenticated).toBe(true)
      expect(store.user.username).toBe('jane')
      expect(window.localStorage.getItem('id_token')).toBe('new-token')
    })

    it('records API errors and re-throws when registration fails', async () => {
      ApiService.post.mockRejectedValue({
        response: { data: { errors: { email: ['has already been taken'] } } },
      })
      const store = useAuthStore()

      await expect(store.register({})).rejects.toBeDefined()

      expect(store.isAuthenticated).toBe(false)
      expect(store.errors).toEqual({ email: ['has already been taken'] })
    })

    it('falls back to the error message when the failure has no API response', async () => {
      ApiService.post.mockRejectedValue(new Error('timeout'))
      const store = useAuthStore()

      await expect(store.register({})).rejects.toThrow('timeout')

      expect(store.errors).toEqual({ error: ['timeout'] })
    })
  })

  describe('checkAuth', () => {
    it('purges auth and makes no request when there is no token', async () => {
      const store = useAuthStore()
      store.isAuthenticated = true

      await store.checkAuth()

      expect(store.isAuthenticated).toBe(false)
      expect(ApiService.setHeader).not.toHaveBeenCalled()
      expect(ApiService.get).not.toHaveBeenCalled()
    })

    it('sends the token, loads the current user and authenticates when a token exists', async () => {
      window.localStorage.setItem('id_token', 'stored')
      ApiService.get.mockResolvedValue({ data: { user: { username: 'jane', token: 'stored' } } })
      const store = useAuthStore()

      await store.checkAuth()

      expect(ApiService.setHeader).toHaveBeenCalled()
      expect(ApiService.get).toHaveBeenCalledWith('user')
      expect(store.isAuthenticated).toBe(true)
      expect(store.user.username).toBe('jane')
    })

    it('records errors (without throwing) when the token is rejected', async () => {
      window.localStorage.setItem('id_token', 'expired')
      ApiService.get.mockRejectedValue({
        response: { data: { errors: { token: ['is invalid'] } } },
      })
      const store = useAuthStore()

      // checkAuth runs at app start-up, so it must never reject.
      await expect(store.checkAuth()).resolves.toBeUndefined()

      expect(store.errors).toEqual({ token: ['is invalid'] })
    })

    it('falls back to the error message when the failure has no API response', async () => {
      window.localStorage.setItem('id_token', 'stored')
      ApiService.get.mockRejectedValue(new Error('offline'))
      const store = useAuthStore()

      await store.checkAuth()

      expect(store.errors).toEqual({ error: ['offline'] })
    })
  })

  describe('updateUser', () => {
    it('PUTs the profile fields and stores the updated user', async () => {
      ApiService.put.mockResolvedValue({
        data: { user: { email: 'new@x.y', username: 'jane', token: 'tok2' } },
      })
      const store = useAuthStore()

      const data = await store.updateUser({
        email: 'new@x.y',
        username: 'jane',
        bio: 'hi',
        image: 'pic.png',
      })

      expect(ApiService.put).toHaveBeenCalledWith('user', {
        email: 'new@x.y',
        username: 'jane',
        bio: 'hi',
        image: 'pic.png',
      })
      expect(store.user.email).toBe('new@x.y')
      expect(window.localStorage.getItem('id_token')).toBe('tok2')
      expect(data.user.username).toBe('jane')
    })

    it('omits the password from the request when it is empty', async () => {
      ApiService.put.mockResolvedValue({ data: { user: { token: 't' } } })

      await useAuthStore().updateUser({ email: 'a@b.c', password: '' })

      // Sending an empty password would overwrite the user's real one.
      expect(ApiService.put.mock.calls[0][1]).not.toHaveProperty('password')
    })

    it('includes the password in the request when one is provided', async () => {
      ApiService.put.mockResolvedValue({ data: { user: { token: 't' } } })

      await useAuthStore().updateUser({ email: 'a@b.c', password: 'secret' })

      expect(ApiService.put.mock.calls[0][1].password).toBe('secret')
    })

    it('ignores fields that are not part of the profile', async () => {
      ApiService.put.mockResolvedValue({ data: { user: { token: 't' } } })

      await useAuthStore().updateUser({ email: 'a@b.c', isAdmin: true })

      expect(ApiService.put.mock.calls[0][1]).not.toHaveProperty('isAdmin')
    })

    it('propagates request failures to the caller', async () => {
      ApiService.put.mockRejectedValue(new Error('422'))

      await expect(useAuthStore().updateUser({})).rejects.toThrow('422')
    })
  })
})
