import { describe, expect, it } from 'vitest'
import { ref } from 'vue'
import { useArticleFilter } from '@/composables/useArticleFilter'

// Small fixture used by most tests.
const makeArticles = () => [
  { title: 'Vue Basics', description: 'Learn components' },
  { title: 'Pinia Stores', description: 'State management for Vue' },
  { title: 'Routing', description: 'Navigate with vue-router' },
]

describe('useArticleFilter', () => {
  it('starts with an empty search term and returns every article', () => {
    const articles = ref(makeArticles())

    const { searchDetails, filterIt } = useArticleFilter(articles)

    expect(searchDetails.value).toBe('')
    // An empty string is "included" in every field, so nothing is filtered out.
    expect(filterIt.value).toHaveLength(3)
  })

  it('filters by title', () => {
    const { searchDetails, filterIt } = useArticleFilter(ref(makeArticles()))

    searchDetails.value = 'pinia'

    expect(filterIt.value.map((a) => a.title)).toEqual(['Pinia Stores'])
  })

  it('filters by description', () => {
    const { searchDetails, filterIt } = useArticleFilter(ref(makeArticles()))

    searchDetails.value = 'components'

    expect(filterIt.value.map((a) => a.title)).toEqual(['Vue Basics'])
  })

  it('matches on either field, so one search can hit title and description of different articles', () => {
    const { searchDetails, filterIt } = useArticleFilter(ref(makeArticles()))

    // "vue" is in the title of article 1, the description of article 2 and 3.
    searchDetails.value = 'vue'

    expect(filterIt.value).toHaveLength(3)
  })

  it('is case-insensitive for both the search text and the article text', () => {
    const { searchDetails, filterIt } = useArticleFilter(ref(makeArticles()))

    searchDetails.value = 'ROUTING'

    expect(filterIt.value.map((a) => a.title)).toEqual(['Routing'])
  })

  it('returns an empty list when nothing matches', () => {
    const { searchDetails, filterIt } = useArticleFilter(ref(makeArticles()))

    searchDetails.value = 'zzz-no-match'

    expect(filterIt.value).toEqual([])
  })

  it('recomputes when the search text changes', () => {
    const { searchDetails, filterIt } = useArticleFilter(ref(makeArticles()))

    searchDetails.value = 'pinia'
    expect(filterIt.value).toHaveLength(1)

    searchDetails.value = ''
    expect(filterIt.value).toHaveLength(3)
  })

  it('recomputes when the source list changes', () => {
    const articles = ref(makeArticles())
    const { searchDetails, filterIt } = useArticleFilter(articles)
    searchDetails.value = 'vue'

    articles.value = [{ title: 'Only Vue', description: '' }]

    expect(filterIt.value.map((a) => a.title)).toEqual(['Only Vue'])
  })

  it('treats a null/undefined list as empty instead of throwing', () => {
    // The store's list can be momentarily undefined (e.g. API returned no `articles` key).
    const { filterIt } = useArticleFilter(ref(undefined))

    expect(filterIt.value).toEqual([])
  })

  it('tolerates items whose fields are null or undefined', () => {
    const articles = ref([{ title: null, description: undefined }, { title: 'Real' }])
    const { searchDetails, filterIt } = useArticleFilter(articles)

    searchDetails.value = 'real'

    expect(filterIt.value).toEqual([{ title: 'Real' }])
  })

  it('accepts a custom getFields function (used by HomeContent to filter plain string tags)', () => {
    const tags = ref(['dragons', 'sushi', 'vue'])
    const { searchDetails, filterIt } = useArticleFilter(tags, (tag) => [tag])

    searchDetails.value = 'su'

    expect(filterIt.value).toEqual(['sushi'])
  })

  it('does not mutate the original array', () => {
    const articles = ref(makeArticles())
    const { searchDetails, filterIt } = useArticleFilter(articles)

    searchDetails.value = 'pinia'
    // Reading the computed value triggers the filter.
    expect(filterIt.value).toHaveLength(1)

    expect(articles.value).toHaveLength(3)
  })
})
