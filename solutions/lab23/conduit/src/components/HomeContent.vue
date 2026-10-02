<template>
  <div class="home-page">
    <div class="banner">
      <div class="container">
        <h1 class="logo-font">conduit</h1>
        <p>A place to share your knowledge.</p>
      </div>
    </div>
    <div class="container page">
      <div class="row">
        <div class="col-md-9">
          <div class="feed-toggle">
            <ul class="nav nav-pills outline-active">
              <li class="nav-item">
                <RouterLink class="nav-link" exact-active-class="active" :to="{ name: 'home' }">
                  Global Feed
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink
                  class="nav-link"
                  exact-active-class="active"
                  :to="{ name: 'popular' }"
                >
                  Most Favorited
                </RouterLink>
              </li>
            </ul>
          </div>
          <RouterView v-slot="{ Component }">
            <component :is="Component" :tag="selectedTag" />
          </RouterView>
        </div>
        <div class="col-md-3">
          <p v-if="isAuthenticated">Welcome, authenticated user</p>
          <input v-model="tagSearch" class="form-control" placeholder="filter tags" />
          <TagList>
            <TagItem
              v-for="tag in filteredTags"
              :key="tag"
              :tag="tag"
              :active="tag === selectedTag"
              @select="selectTag"
            />
          </TagList>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { RouterLink, RouterView } from 'vue-router'
import TagList from './TagList.vue'
import TagItem from './TagItem.vue'
import ApiService from '../common/api.service'
import { useArticleFilter } from '../composables/useArticleFilter'
import { useHomeStore } from '../stores/home'
import { useAuthStore } from '@/stores/auth'

const { isAuthenticated } = storeToRefs(useAuthStore())
const homeStore = useHomeStore()
const { tags } = storeToRefs(homeStore)
const { searchDetails: tagSearch, filterIt: filteredTags } = useArticleFilter(tags, (tag) => [tag])
const selectedTag = ref('')

function selectTag(tag) {
  selectedTag.value = selectedTag.value === tag ? '' : tag
}

onMounted(async () => {
  const { data } = await ApiService.query('tags')
  homeStore.setTags(data.tags)
})
</script>
<style scoped>
.banner {
  background: #5cb85c;
}

.banner p {
  color: #fff;
  text-align: center;
  font-size: 1.5rem;
  font-weight: 300;
}

.banner h1 {
  font-weight: 700;
  text-align: center;
  font-size: 3.5rem;
}
.sidebar {
  padding: 5px 10px 10px;
  background: #f3f3f3;
  border-radius: 4px;
}

.feed-toggle {
}
.sidebar p {
}
</style>
