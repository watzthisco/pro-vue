Lab 18: Slots
In this lab, you’ll load the popular tags from the API, display them with slots, show each article's tags, and make clicking a tag filter the article list.
☐   1.	Create a new component, src/components/TagItem.vue, that displays a single tag.
<template>
  <li class="tag-default tag-pill tag-outline">{{ tag }}</li>
</template>
<script setup>
defineProps({
  tag: { type: String, required: true },
})
</script>
☐   2.	Create src/components/TagList.vue. It owns the layout (the sidebar box, the heading, and the <ul>), but not the content. Use a <slot> where the tags go, with fallback text for when the parent supplies nothing.
<template>
  <div class="sidebar">
    <p>Popular Tags</p>
    <ul class="tag-list">
      <slot>No tags available.</slot>
    </ul>
  </div>
</template>
☐   3.	In HomeContent.vue, import ApiService, TagList, TagItem, and onMounted/ref. Add a tags ref and load the tags from the /tags endpoint (same base URL as the articles feed).
const tags = ref([])

onMounted(async () => {
  const { data } = await ApiService.query('tags')
  tags.value = data.tags
})
☐   4.	Replace the hard-coded sidebar markup in HomeContent.vue with TagList, and supply the tags through its default slot.
<TagList>
  <TagItem v-for="tag in tags" :key="tag" :tag="tag" />
</TagList>
Reload the page. The tags from the API should appear in the second column.
☐   5.	In ArticlePreview.vue, add a named slot called tags beneath the “Read more...” link.
<slot name="tags" />
☐   6.	In ArticleList.vue, fill the tags slot of each ArticlePreview with the article's tagList. Use the #tags shorthand for v-slot:tags.
<ArticlePreview ...>
  <template #tags>
    <ul class="tag-list">
      <li
        v-for="t in article.tagList"
        :key="t"
        class="tag-default tag-pill tag-outline"
      >
        {{ t }}
      </li>
    </ul>
  </template>
</ArticlePreview>
☐   7.	Make TagItem.vue emit an event when clicked. Use defineEmits and emit the tag name.
<li class="tag-default tag-pill tag-outline" @click="emit('select', tag)">
  {{ tag }}
</li>
const emit = defineEmits(['select'])
☐   8.	In HomeContent.vue, add a selectedTag ref and a handler. Clicking the selected tag a second time clears the filter.
const selectedTag = ref('')

function selectTag(tag) {
  selectedTag.value = selectedTag.value === tag ? '' : tag
}
Listen for the event on each TagItem:
<TagItem v-for="tag in tags" :key="tag" :tag="tag" @select="selectTag" />
☐   9.	Pass selectedTag down to the article list. Add a tag prop to GlobalFeed.vue and ArticleList.vue.
In HomeContent.vue:
<GlobalFeed :tag="selectedTag" />
In GlobalFeed.vue:
defineProps({ tag: { type: String, default: '' } })
<ArticleList type="all" :tag="tag" />
In ArticleList.vue:
const props = defineProps({ tag: { type: String, default: '' } })
☐   10.	Update the filterIt computed property in ArticleList.vue so it also checks the selected tag.
const filterIt = computed(() => {
  const term = searchDetails.value.toLowerCase()
  return articles.value.filter(
    (article) =>
      (!props.tag || (article.tagList ?? []).includes(props.tag)) &&
      (article.title.toLowerCase().includes(term) ||
        (article.description ?? '').toLowerCase().includes(term)),
  )
})
☐   11.	Start up your development server. Verify that tags load, each article lists its tags, and clicking a tag filters the list.
☐   12.	Add an active class to TagItem.vue so the selected tag is highlighted. Add an active Boolean prop and pass :active="tag === selectedTag" from HomeContent.vue.
☐   13.	Challenge: allow more than one tag to be selected at once. Change selectedTag to an array, and show only articles that have all of the selected tags. Add a “Clear filters” button, supplied to TagList through a second named slot called footer.
☐   14.	Challenge: turn TagList into a scoped-slot component that fetches its own tags. Move the ApiService call from HomeContent.vue into TagList.vue, and expose { tags, loading, error } to the parent with slot props (<slot :tags="tags" :loading="loading" :error="error">). In HomeContent.vue, use v-slot="{ tags, loading, error }" to render a “Loading...” message, an error message, or the list of TagItem components.
