Lab 17: Forms
In this lab, you’ll implement an input box that filters the currently displayed list of articles based on the text entered into it.
☐   1.	Create an input in the ArticleList component and bind it with v-model.
<input
  v-model="searchDetails"
  class="form-control"
  placeholder="filter articles"
/>
Note: the earlier version of this lab used v-model.number. That modifier casts the input to a number, which is wrong here — we are filtering on text. Leave it off.
☐   2.	Add a ref named searchDetails to hold the search text.
const searchDetails = ref('');
☐   3.	Import computed and make a computed property in ArticleList called filterIt.
const filterIt = computed(() =>
  articles.value.filter((article) =>
    article.title.includes(searchDetails.value),
  ),
);
Both refs are read with .value inside the computed callback. Because this is an arrow function there is no this to capture, so the "var self = this" trick the Options API version needed is gone.
☐   4.	Modify the v-for directive in ArticleList.vue to use filterIt instead of articles:
v-for="(article, index) in filterIt"
☐   5.	Start up your development server and try typing letters into the search form to see how the list is filtered.
☐   6.	Challenge: make the search case-insensitive.
☐   7.	Challenge: make the search consider the description text as well as the title.
