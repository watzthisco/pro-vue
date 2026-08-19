import { computed, ref } from 'vue';

/**
 * Filters a reactive list of articles by title.
 *
 * This is the Composition API replacement for a mixin: the caller passes in
 * the state the composable needs and gets back only what it returns, so
 * there is no implicit merging of component options.
 *
 * @param {import('vue').Ref<Array>} articles reactive list of articles
 */
export function useArticleFilter(articles) {
  const searchDetails = ref('');

  const filterIt = computed(() =>
    (articles.value ?? []).filter((article) =>
      article.title.includes(searchDetails.value),
    ),
  );

  return { searchDetails, filterIt };
}
