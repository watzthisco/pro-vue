import { describe, expect, it } from 'vitest';
import { mount } from '@vue/test-utils';

import Home from '@/components/Home.vue';

const createWrapper = () => mount(Home);

describe('Home', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper();

    expect(wrapper.exists()).toBe(true);
  });
});
