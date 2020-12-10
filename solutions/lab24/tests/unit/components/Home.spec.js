import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router';
import Vuex from "vuex";


import Home from "../../../src/components/Home.vue";

const localVue = createLocalVue()
localVue.use(VueRouter);
localVue.use(Vuex);
const store = new Vuex.Store()
const router = new VueRouter();

const createWrapper = () => {
    return shallowMount(Home, {
      store,
      router,
      localVue    
    });
  };

describe("Home", () => {
    it("should render without a problem", () => {
        const wrapper = createWrapper();
        expect(wrapper.exists()).toBe(true)
      });    
})
