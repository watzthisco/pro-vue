import { beforeEach, describe, expect, it } from 'vitest';
import { shallowMount } from '@vue/test-utils';
import { createPinia, setActivePinia } from 'pinia';
import { createRouter, createWebHistory } from 'vue-router';

import Home from '@/components/Home.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [{ name: 'home', path: '/', component: { template: '<div />' } }],
});

let pinia;

beforeEach(() => {
  // A fresh Pinia per test keeps store state from leaking between specs.
  pinia = createPinia();
  setActivePinia(pinia);
});

const createWrapper = () =>
  shallowMount(Home, { global: { plugins: [pinia, router] } });

describe('Home', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper();

    expect(wrapper.exists()).toBe(true);
  });
});
