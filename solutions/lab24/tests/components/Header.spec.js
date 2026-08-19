import { describe, expect, it } from 'vitest';
import { mount } from '@vue/test-utils';
import { createRouter, createWebHistory } from 'vue-router';

import Header from '@/components/Header.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { name: 'home', path: '/', component: { template: '<div />' } },
    { name: 'login', path: '/login', component: { template: '<div />' } },
    { name: 'register', path: '/register', component: { template: '<div />' } },
  ],
});

const createWrapper = () => mount(Header, { global: { plugins: [router] } });

describe('Header', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper();

    expect(wrapper.exists()).toBe(true);
  });
});
