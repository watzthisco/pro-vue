import { beforeEach, describe, expect, it, vi } from 'vitest'
import { flushPromises } from '@vue/test-utils'

// main.js has side effects (it creates and mounts the app as soon as it is imported), so we
// provide the mount point, mock the HTTP layer, and import a fresh copy for each test.
vi.mock('@/common/api.service', () => ({
  default: {
    init: vi.fn(),
    query: vi.fn(),
    post: vi.fn(),
    get: vi.fn(),
    put: vi.fn(),
    setHeader: vi.fn(),
  },
  ArticlesService: { query: vi.fn() },
}))

import ApiService, { ArticlesService } from '@/common/api.service'

// The first navigation loads lazy route components, so wait for the router (the same
// instance main.js uses, since modules are cached after resetModules) before asserting.
async function settleRouter() {
  const { default: router } = await import('@/router')
  await router.isReady()
  await flushPromises()
}

beforeEach(() => {
  vi.resetModules()
  vi.clearAllMocks()
  window.localStorage.clear()
  document.body.innerHTML = '<div id="app"></div>'
  ApiService.query.mockResolvedValue({ data: { tags: [] } })
  ArticlesService.query.mockResolvedValue({ data: { articles: [], articlesCount: 0 } })
  window.history.pushState({}, '', '/')
})

describe('main.js (application bootstrap)', () => {
  it('initialises the API service', async () => {
    await import('@/main')

    expect(ApiService.init).toHaveBeenCalledTimes(1)
  })

  it('mounts the app into #app with the header, home page and footer', async () => {
    await import('@/main')
    await settleRouter()

    const root = document.querySelector('#app')
    expect(root.querySelector('nav.navbar')).not.toBeNull()
    expect(root.querySelector('.home-page')).not.toBeNull()
    expect(root.querySelector('footer')).not.toBeNull()
  })

  it('shows the logged-out navigation when there is no saved token', async () => {
    await import('@/main')
    await settleRouter()

    const text = document.querySelector('nav').textContent
    expect(text).toContain('Sign In')
    expect(text).not.toContain('Log out')
  })

  it('restores the session on start-up when a token is saved', async () => {
    // checkAuth() should send the saved token and then ask the API who the user is.
    window.localStorage.setItem('id_token', 'saved')
    ApiService.get.mockResolvedValue({ data: { user: { username: 'jane', token: 'saved' } } })

    await import('@/main')
    await settleRouter()

    expect(ApiService.setHeader).toHaveBeenCalled()
    expect(ApiService.get).toHaveBeenCalledWith('user')
    expect(document.querySelector('nav').textContent).toContain('Log out')
  })
})
