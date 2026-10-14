import { afterEach, describe, expect, it, vi } from 'vitest'

// config.js reads import.meta.env at import time, so each test stubs the environment
// first and then imports a *fresh* copy of the module (vi.resetModules clears the cache).
afterEach(() => {
  vi.unstubAllEnvs()
  vi.resetModules()
})

describe('config', () => {
  it('falls back to the public RealWorld API when VITE_API_URL is not set', async () => {
    // Stubbing with undefined removes the variable, simulating a project with no .env file.
    vi.stubEnv('VITE_API_URL', undefined)
    vi.resetModules()

    const { API_URL } = await import('@/common/config')

    expect(API_URL).toBe('https://api.realworld.show/api')
  })

  it('uses VITE_API_URL when it is provided', async () => {
    vi.stubEnv('VITE_API_URL', 'http://localhost:3000/api')
    vi.resetModules()

    const { API_URL } = await import('@/common/config')

    expect(API_URL).toBe('http://localhost:3000/api')
  })

  it('exports the URL as both a named and a default export', async () => {
    vi.stubEnv('VITE_API_URL', 'http://example.test/api')
    vi.resetModules()

    const config = await import('@/common/config')

    expect(config.default).toBe(config.API_URL)
  })
})
