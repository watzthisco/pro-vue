import { beforeEach, describe, expect, it } from 'vitest'
import JwtService, { destroyToken, getToken, saveToken } from '@/common/jwt.service'

// The JWT service is a thin wrapper around window.localStorage. jsdom provides a
// real localStorage implementation, so we exercise it directly instead of mocking it.
beforeEach(() => {
  // Start every test with an empty storage so tests cannot leak state into each other.
  window.localStorage.clear()
})

describe('jwt.service', () => {
  it('returns null when no token has been saved', () => {
    // localStorage.getItem returns null for missing keys; callers rely on this
    // (e.g. the auth store uses `!!getToken()` to decide if the user is logged in).
    expect(getToken()).toBeNull()
  })

  it('saves a token under the "id_token" key', () => {
    saveToken('abc123')

    // Checking the raw storage key guards against someone renaming the key by accident,
    // which would silently log every existing user out.
    expect(window.localStorage.getItem('id_token')).toBe('abc123')
  })

  it('reads back a token that was saved', () => {
    saveToken('abc123')

    expect(getToken()).toBe('abc123')
  })

  it('overwrites a previously saved token', () => {
    saveToken('old')
    saveToken('new')

    expect(getToken()).toBe('new')
  })

  it('removes the token when destroyed', () => {
    saveToken('abc123')

    destroyToken()

    expect(getToken()).toBeNull()
    expect(window.localStorage.getItem('id_token')).toBeNull()
  })

  it('does not throw when destroying a token that does not exist', () => {
    // Logging out twice (or logging out with no token) should be a harmless no-op.
    expect(() => destroyToken()).not.toThrow()
  })

  it('exposes the same functions on the default export', () => {
    // Some modules import the default object (`JwtService.getToken()`), others import the
    // named functions. Both styles must behave identically.
    expect(JwtService.getToken).toBe(getToken)
    expect(JwtService.saveToken).toBe(saveToken)
    expect(JwtService.destroyToken).toBe(destroyToken)
  })
})
