import { beforeEach, describe, expect, it, vi } from 'vitest'
import { flushPromises, mount } from '@vue/test-utils'
import { createPinia, setActivePinia } from 'pinia'
import { createMemoryHistory, createRouter } from 'vue-router'
import ApiService from '@/common/api.service'
import HomeContent from '@/components/HomeContent.vue'
import TagItem from '@/components/TagItem.vue'
import { useAuthStore } from '@/stores/auth'
import { useHomeStore } from '@/stores/home'

// HomeContent requests /tags on mount, so keep the test off the network.
vi.mock('@/common/api.service', () => ({
  default: {
    query: vi.fn(),
    post: vi.fn(),
    get: vi.fn(),
    put: vi.fn(),
    setHeader: vi.fn(),
  },
}))

// The routed child records the `tag` prop it receives, so we can verify HomeContent
// forwards the selected tag to whatever page is shown in its <RouterView>.
const FeedStub = {
  props: { tag: { type: String, default: '' } },
  template: '<div class="feed-stub">{{ tag }}</div>',
}

let pinia
let router

beforeEach(async () => {
  window.localStorage.clear()
  vi.clearAllMocks()
  ApiService.query.mockResolvedValue({ data: { tags: ['vue', 'pinia', 'sushi'] } })
  pinia = createPinia()
  setActivePinia(pinia)
  router = createRouter({
    history: createMemoryHistory(),
    routes: [
      {
        path: '/',
        component: HomeContent,
        children: [
          { name: 'home', path: '', component: FeedStub },
          { name: 'popular', path: 'popular', component: FeedStub },
        ],
      },
    ],
  })
  await router.push('/')
  await router.isReady()
})

// Mounts the real HomeContent through the router and waits for the tag request to finish.
async function createWrapper() {
  const wrapper = mount({ template: '<RouterView />' }, { global: { plugins: [pinia, router] } })
  await flushPromises()
  return wrapper
}

const tagTexts = (wrapper) => wrapper.findAllComponents(TagItem).map((t) => t.text())

describe('HomeContent', () => {
  it('should render without a problem', async () => {
    const wrapper = await createWrapper()

    expect(wrapper.find('.home-page').exists()).toBe(true)
  })

  describe('banner and navigation', () => {
    it('shows the site banner', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.find('.banner h1').text()).toBe('conduit')
      expect(wrapper.find('.banner p').text()).toBe('A place to share your knowledge.')
    })

    it('shows Global Feed and Most Favorited tabs', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.findAll('.nav-link').map((a) => a.text())).toEqual([
        'Global Feed',
        'Most Favorited',
      ])
    })

    it('highlights the tab for the current route', async () => {
      const wrapper = await createWrapper()
      const tabs = wrapper.findAll('.nav-link')

      expect(tabs[0].classes()).toContain('active')
      expect(tabs[1].classes()).not.toContain('active')

      await router.push('/popular')

      expect(tabs[0].classes()).not.toContain('active')
      expect(tabs[1].classes()).toContain('active')
    })

    it('renders the routed child inside the page', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.find('.feed-stub').exists()).toBe(true)
    })
  })

  describe('authentication message', () => {
    it('is hidden for anonymous visitors', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.text()).not.toContain('Welcome, authenticated user')
    })

    it('is shown to authenticated users', async () => {
      useAuthStore().isAuthenticated = true

      const wrapper = await createWrapper()

      expect(wrapper.text()).toContain('Welcome, authenticated user')
    })
  })

  describe('tags', () => {
    it('requests the tag list from the API on mount', async () => {
      await createWrapper()

      expect(ApiService.query).toHaveBeenCalledWith('tags')
    })

    it('saves the fetched tags in the home store', async () => {
      await createWrapper()

      expect(useHomeStore().tags).toEqual(['vue', 'pinia', 'sushi'])
    })

    it('renders one TagItem per tag', async () => {
      const wrapper = await createWrapper()

      expect(tagTexts(wrapper)).toEqual(['vue', 'pinia', 'sushi'])
    })

    it('shows the TagList fallback text when there are no tags', async () => {
      ApiService.query.mockResolvedValue({ data: { tags: [] } })

      const wrapper = await createWrapper()

      expect(wrapper.find('.sidebar').text()).toContain('No tags available.')
    })

    it('filters the visible tags by the typed text', async () => {
      const wrapper = await createWrapper()

      await wrapper.find('input[placeholder="filter tags"]').setValue('su')

      expect(tagTexts(wrapper)).toEqual(['sushi'])
    })

    it('matches tags case-insensitively', async () => {
      const wrapper = await createWrapper()

      await wrapper.find('input[placeholder="filter tags"]').setValue('PINIA')

      expect(tagTexts(wrapper)).toEqual(['pinia'])
    })
  })

  describe('selecting a tag', () => {
    it('forwards an empty tag to the feed by default', async () => {
      const wrapper = await createWrapper()

      expect(wrapper.find('.feed-stub').text()).toBe('')
    })

    it('marks the clicked tag as active and passes it to the feed', async () => {
      const wrapper = await createWrapper()

      await wrapper.findAllComponents(TagItem)[1].trigger('click')

      const items = wrapper.findAllComponents(TagItem)
      expect(items.map((t) => t.props('active'))).toEqual([false, true, false])
      expect(wrapper.find('.feed-stub').text()).toBe('pinia')
    })

    it('un-selects the tag when it is clicked a second time', async () => {
      const wrapper = await createWrapper()
      const first = () => wrapper.findAllComponents(TagItem)[0]

      await first().trigger('click')
      await first().trigger('click')

      expect(first().props('active')).toBe(false)
      expect(wrapper.find('.feed-stub').text()).toBe('')
    })

    it('switches the selection when a different tag is clicked', async () => {
      const wrapper = await createWrapper()

      await wrapper.findAllComponents(TagItem)[0].trigger('click')
      await wrapper.findAllComponents(TagItem)[2].trigger('click')

      expect(wrapper.find('.feed-stub').text()).toBe('sushi')
    })

    it('keeps the selected tag when switching between Global Feed and Most Favorited', async () => {
      const wrapper = await createWrapper()
      await wrapper.findAllComponents(TagItem)[0].trigger('click')

      await router.push('/popular')

      expect(wrapper.find('.feed-stub').text()).toBe('vue')
    })
  })
})
