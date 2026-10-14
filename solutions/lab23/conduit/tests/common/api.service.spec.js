import { beforeEach, describe, expect, it, vi } from 'vitest'

// vi.hoisted runs before the (hoisted) vi.mock factory, so the fake axios client is
// available when api.service.js calls `axios.create()` at import time.
const { client } = vi.hoisted(() => ({
  client: {
    defaults: { baseURL: '', headers: { common: {} } },
    get: vi.fn(),
    post: vi.fn(),
    put: vi.fn(),
    delete: vi.fn(),
  },
}))

vi.mock('axios', () => ({ default: { create: vi.fn(() => client) } }))

import axios from 'axios'
import ApiService, {
  ArticlesService,
  CommentsService,
  FavoriteService,
  TagsService,
} from '@/common/api.service'
import JwtService from '@/common/jwt.service'
import { API_URL } from '@/common/config'

// Capture the axios.create() call made at import time, before any mockReset below.
const createCallArgs = vi.mocked(axios.create).mock.calls[0]

beforeEach(() => {
  // Reset the fake HTTP methods (but keep the client object itself) between tests.
  client.get.mockReset().mockResolvedValue({ data: {} })
  client.post.mockReset().mockResolvedValue({ data: {} })
  client.put.mockReset().mockResolvedValue({ data: {} })
  client.delete.mockReset().mockResolvedValue({ data: {} })
  client.defaults.headers.common = {}
  window.localStorage.clear()
})

describe('ApiService', () => {
  it('creates an axios client that points at the configured API URL', () => {
    expect(createCallArgs).toEqual([{ baseURL: API_URL }])
  })

  it('init() re-applies the base URL to the client defaults', () => {
    client.defaults.baseURL = 'changed'

    ApiService.init()

    expect(client.defaults.baseURL).toBe(API_URL)
  })

  it('setHeader() sends the stored JWT in the Authorization header', () => {
    JwtService.saveToken('my-token')

    ApiService.setHeader()

    // The RealWorld API expects the "Token <jwt>" scheme, not "Bearer".
    expect(client.defaults.headers.common.Authorization).toBe('Token my-token')
  })

  describe('query()', () => {
    it('GETs the resource, forwarding params to axios', async () => {
      const response = { data: { articles: [] } }
      client.get.mockResolvedValue(response)

      const result = await ApiService.query('articles', { params: { limit: 5 } })

      expect(client.get).toHaveBeenCalledWith('articles', { params: { limit: 5 } })
      expect(result).toBe(response)
    })

    it('wraps failures in a descriptive Error', async () => {
      client.get.mockRejectedValue(new Error('Network Error'))

      await expect(ApiService.query('articles')).rejects.toThrow(
        '[RWV] ApiService Error: Network Error',
      )
    })
  })

  describe('get()', () => {
    it('GETs just the resource when no slug is given', async () => {
      await ApiService.get('tags')

      expect(client.get).toHaveBeenCalledWith('tags')
    })

    it('appends the slug to the resource path when one is given', async () => {
      await ApiService.get('articles', 'my-slug')

      expect(client.get).toHaveBeenCalledWith('articles/my-slug')
    })

    it('wraps failures in a descriptive Error', async () => {
      client.get.mockRejectedValue(new Error('boom'))

      await expect(ApiService.get('tags')).rejects.toThrow('[RWV] ApiService Error: boom')
    })
  })

  describe('post()', () => {
    it('POSTs the params to the resource', async () => {
      await ApiService.post('users', { user: { email: 'a@b.c' } })

      expect(client.post).toHaveBeenCalledWith('users', { user: { email: 'a@b.c' } })
    })

    it('does NOT wrap errors, so callers can inspect error.response (used by the auth store)', async () => {
      const error = { response: { data: { errors: { email: ['is taken'] } } } }
      client.post.mockRejectedValue(error)

      await expect(ApiService.post('users', {})).rejects.toBe(error)
    })
  })

  describe('update() and put()', () => {
    it('update() PUTs to resource/slug', async () => {
      await ApiService.update('articles', 'my-slug', { article: { title: 'T' } })

      expect(client.put).toHaveBeenCalledWith('articles/my-slug', { article: { title: 'T' } })
    })

    it('put() PUTs to the bare resource', async () => {
      await ApiService.put('user', { bio: 'hi' })

      expect(client.put).toHaveBeenCalledWith('user', { bio: 'hi' })
    })
  })

  describe('delete()', () => {
    it('sends a DELETE to the resource', async () => {
      await ApiService.delete('articles/my-slug')

      expect(client.delete).toHaveBeenCalledWith('articles/my-slug')
    })

    it('wraps failures in a descriptive Error', async () => {
      client.delete.mockRejectedValue(new Error('forbidden'))

      await expect(ApiService.delete('articles/x')).rejects.toThrow(
        '[RWV] ApiService Error: forbidden',
      )
    })
  })
})

describe('TagsService', () => {
  it('get() fetches the "tags" resource', async () => {
    await TagsService.get()

    expect(client.get).toHaveBeenCalledWith('tags')
  })
})

describe('ArticlesService', () => {
  it('query("all") requests /articles with the given filters as params', async () => {
    await ArticlesService.query('all', { limit: 10 })

    expect(client.get).toHaveBeenCalledWith('articles', { params: { limit: 10 } })
  })

  it('query("feed") requests the personal /articles/feed endpoint', async () => {
    await ArticlesService.query('feed', { offset: 0 })

    expect(client.get).toHaveBeenCalledWith('articles/feed', { params: { offset: 0 } })
  })

  it('query() treats any non-"feed" type as the global article list', async () => {
    await ArticlesService.query(undefined, undefined)

    expect(client.get).toHaveBeenCalledWith('articles', { params: undefined })
  })

  it('get() fetches a single article by slug', async () => {
    await ArticlesService.get('hello-world')

    expect(client.get).toHaveBeenCalledWith('articles/hello-world')
  })

  it('create() POSTs the article wrapped in an { article } envelope', async () => {
    await ArticlesService.create({ title: 'T', body: 'B' })

    expect(client.post).toHaveBeenCalledWith('articles', { article: { title: 'T', body: 'B' } })
  })

  it('update() PUTs the changed article wrapped in an { article } envelope', async () => {
    await ArticlesService.update('hello-world', { title: 'New' })

    expect(client.put).toHaveBeenCalledWith('articles/hello-world', { article: { title: 'New' } })
  })

  it('destroy() DELETEs the article by slug', async () => {
    await ArticlesService.destroy('hello-world')

    expect(client.delete).toHaveBeenCalledWith('articles/hello-world')
  })
})

describe('CommentsService', () => {
  it('get() fetches the comments of an article', async () => {
    await CommentsService.get('hello-world')

    expect(client.get).toHaveBeenCalledWith('articles/hello-world/comments')
  })

  it('get() throws synchronously when the slug is not a string', () => {
    // Guard clause: prevents requests to ".../undefined/comments".
    expect(() => CommentsService.get(undefined)).toThrow('article slug required')
    expect(() => CommentsService.get(42)).toThrow('article slug required')
    expect(client.get).not.toHaveBeenCalled()
  })

  it('post() wraps the text in a { comment: { body } } envelope', async () => {
    await CommentsService.post('hello-world', 'Nice post!')

    expect(client.post).toHaveBeenCalledWith('articles/hello-world/comments', {
      comment: { body: 'Nice post!' },
    })
  })

  it('destroy() DELETEs a single comment by id', async () => {
    await CommentsService.destroy('hello-world', 7)

    expect(client.delete).toHaveBeenCalledWith('articles/hello-world/comments/7')
  })
})

describe('FavoriteService', () => {
  it('add() POSTs to the favorite endpoint of the article', async () => {
    await FavoriteService.add('hello-world')

    expect(client.post).toHaveBeenCalledWith('articles/hello-world/favorite', undefined)
  })

  it('remove() DELETEs the favorite endpoint of the article', async () => {
    await FavoriteService.remove('hello-world')

    expect(client.delete).toHaveBeenCalledWith('articles/hello-world/favorite')
  })
})
