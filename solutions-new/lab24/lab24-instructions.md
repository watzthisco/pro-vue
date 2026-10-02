# Lab 24: Transitions and Animations

Vue's built-in `<Transition>` component applies CSS classes at each stage of an element entering or leaving the DOM, so you can animate it with plain CSS.

> **Note:** the class names changed in Vue 3. What Vue 2 called `v-enter` is now `v-enter-from`, and what it called `v-leave` is now `v-leave-from`. (`v-leave-to` is unchanged.) If you copy an example from an old blog post and nothing animates, this is usually why.

1. Add a Remove From Feed icon (maybe a trash can) to each article.

2. When clicked, it should remove the article from the feed.

3. Wrap the list in a `<TransitionGroup>` and animate articles as they leave.

   ```vue
   <TransitionGroup name="article" tag="div">
     <ArticlePreview
       v-for="article in visibleArticles"
       :key="article.slug"
       :article="article"
     />
   </TransitionGroup>
   ```

   Every child of a `<TransitionGroup>` needs a stable, unique key. Using the array index will make the animation attach to the wrong element.

4. Write the transition classes.

   ```css
   .article-enter-from,
   .article-leave-to {
     opacity: 0;
     transform: translateX(30px);
   }

   .article-enter-active,
   .article-leave-active {
     transition: all 0.3s ease;
   }
   ```

5. **Challenge:** add `.article-move` so the remaining articles slide up smoothly to fill the gap.

   > **Hint:** the move transition only works if leaving items are taken out of the layout flow. Give `.article-leave-active` `position: absolute` and a `width`, and make the `<TransitionGroup>` container `position: relative`.
