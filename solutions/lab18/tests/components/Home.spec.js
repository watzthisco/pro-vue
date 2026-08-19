import { describe, expect, it } from 'vitest';
import { shallowMount } from '@vue/test-utils';

import Home from '@/components/Home.vue';

// shallowMount stubs child components, so no HTTP request is made.
const createWrapper = () => shallowMount(Home);

describe('Home', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper();

    expect(wrapper.exists()).toBe(true);
  });
});
