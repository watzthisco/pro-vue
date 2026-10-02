import { computed, ref } from 'vue'

const defaultFields = (article) => [article.title, article.description]

// getFields returns the strings of an item that the search text is matched against.
export function useArticleFilter(articles, getFields = defaultFields) {
  const searchDetails = ref('')

  const filterIt = computed(() => {
    const term = searchDetails.value.toLowerCase()
    return (articles.value ?? []).filter((article) =>
      getFields(article).some((field) => (field ?? '').toLowerCase().includes(term)),
    )
  })

  return { searchDetails, filterIt }
}
