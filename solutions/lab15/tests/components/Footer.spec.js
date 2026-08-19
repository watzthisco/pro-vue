import { describe, expect, it } from 'vitest';
import { mount } from '@vue/test-utils';

import Footer from '@/components/Footer.vue';

const createWrapper = () => mount(Footer);

describe('Footer', () => {
  it('should render without a problem', () => {
    const wrapper = createWrapper();

    expect(wrapper.exists()).toBe(true);
  });
});
