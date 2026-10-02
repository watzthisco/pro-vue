import { beforeEach, describe, expect, it, vi } from 'vitest'
import { createPinia, setActivePinia } from 'pinia'
import ApiService from '@/common/api.service'
import { useAuthStore } from '@/stores/auth'

vi.mock('@/common/api.service', () => ({
  default: { post: vi.fn(), get: vi.fn(), put: vi.fn(), setHeader: vi.fn() },
}))

beforeEach(() => {
  window.localStorage.clear()
  vi.clearAllMocks()
  setActivePinia(createPinia())
})

describe('auth store', () => {
  it('starts unauthenticated when there is no stored token', () => {
    expect(useAuthStore().isAuthenticated).toBe(false)
  })

  it('stores the user and token after a successful login', async () => {
    ApiService.post.mockResolvedValue({ data: { user: { email: 'a@b.c', token: 'abc' } } })
    const store = useAuthStore()

    await store.login({ email: 'a@b.c', password: 'pw' })

    expect(ApiService.post).toHaveBeenCalledWith('users/login', {
      user: { email: 'a@b.c', password: 'pw' },
    })
    expect(store.isAuthenticated).toBe(true)
    expect(store.user.email).toBe('a@b.c')
    expect(window.localStorage.getItem('id_token')).toBe('abc')
  })

  it('records errors and re-throws when login fails', async () => {
    ApiService.post.mockRejectedValue({
      response: { data: { errors: { 'email or password': ['is invalid'] } } },
    })
    const store = useAuthStore()

    await expect(store.login({ email: 'x', password: 'y' })).rejects.toBeDefined()

    expect(store.isAuthenticated).toBe(false)
    expect(store.errors).toEqual({ 'email or password': ['is invalid'] })
  })

  it('clears the user and token on logout', async () => {
    ApiService.post.mockResolvedValue({ data: { user: { token: 'abc' } } })
    const store = useAuthStore()
    await store.login({})

    store.logout()

    expect(store.isAuthenticated).toBe(false)
    expect(window.localStorage.getItem('id_token')).toBeNull()
  })
})
