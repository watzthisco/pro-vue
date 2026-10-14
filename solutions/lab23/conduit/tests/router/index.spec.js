import { beforeEach, describe, expect, it, vi } from 'vitest'
import router from '@/router'

// Importing the real route components pulls in the API service; keep it off the network.
vi.mock('@/common/api.service', () => ({
  default: { query: vi.fn(), post: vi.fn(), get: vi.fn(), put: vi.fn(), setHeader: vi.fn() },
  ArticlesService: { query: vi.fn() },
}))

beforeEach(async () => {
  // The router is a singleton, so reset it to a known starting point for each test.
  await router.push('/')
  await router.isReady()
})

describe('router', () => {
  describe('route table', () => {
    const names = () => router.getRoutes().map((r) => r.name)

    it('defines the home, popular, login and register routes', () => {
      expect(names()).toEqual(expect.arrayContaining(['home', 'popular', 'login', 'register']))
    })

    it('resolves each named route to its URL', () => {
      expect(router.resolve({ name: 'home' }).path).toBe('/')
      expect(router.resolve({ name: 'popular' }).path).toBe('/popular')
      expect(router.resolve({ name: 'login' }).path).toBe('/login')
      expect(router.resolve({ name: 'register' }).path).toBe('/register')
    })

    it('nests the home and popular feeds inside the HomeContent layout', () => {
      // Two matched records = the parent layout route + the child feed route.
      expect(router.resolve('/').matched).toHaveLength(2)
      expect(router.resolve('/popular').matched).toHaveLength(2)
    })

    it('renders login and register as top-level pages (no parent layout)', () => {
      expect(router.resolve('/login').matched).toHaveLength(1)
      expect(router.resolve('/register').matched).toHaveLength(1)
    })

    it('does not match unknown URLs', () => {
      expect(router.resolve('/does-not-exist').matched).toHaveLength(0)
    })
  })

  describe('navigation', () => {
    it.each([
      ['/', 'home'],
      ['/popular', 'popular'],
      ['/login', 'login'],
      ['/register', 'register'],
    ])('navigating to %s activates the "%s" route', async (path, name) => {
      await router.push(path)

      expect(router.currentRoute.value.name).toBe(name)
    })
  })

  describe('lazy loaded components', () => {
    // Every route uses `() => import(...)`. Calling the loader proves that the file exists,
    // compiles, and has a default export Vue can render.
    // We read the loaders from router.options.routes (the original config) because vue-router
    // replaces them with the resolved components on the live route records once visited.
    const collect = (routes) =>
      routes.flatMap((route) => [route.component, ...collect(route.children ?? [])])
    const loaders = () => collect(router.options.routes)

    it('has a component for every route', () => {
      expect(loaders().length).toBeGreaterThanOrEqual(5)
    })

    it('resolves every route component loader to a component', async () => {
      for (const load of loaders()) {
        const module = await load()
        expect(module.default).toBeDefined()
      }
    })
  })
})
