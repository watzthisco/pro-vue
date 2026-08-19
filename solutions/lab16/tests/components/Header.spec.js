import { describe, expect, it } from 'vitest';
import { mount } from '@vue/test-utils';

import Header from '@/components/Header.vue';

const createWrapper = () => mount(Header);

describe('Header', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper();

    expect(wrapper.exists()).toBe(true);
  });
});
