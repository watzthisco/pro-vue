import { describe, expect, it } from 'vitest';
import { shallowMount } from '@vue/test-utils';

import HelloWorld from '@/components/HelloWorld.vue';

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message';
    // `propsData` was renamed to `props` in Vue Test Utils 2.
    const wrapper = shallowMount(HelloWorld, { props: { msg } });

    expect(wrapper.text()).toMatch(msg);
  });
});
