import Vue from 'vue'
import Vuex from 'vuex'
import actions from './action'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // rss feeds
    origins: [],
    // feeds' tags
    originTags: {}
  },
  mutations: {
    addOrigin (state, { originName, feedLink }) {
      let origin = { originName, feedLink }
      state.origins = state.origins.concat(origin)
    },
    addOriginTags (state, { originName, tags }) {
      Vue.set(state.originTags, originName, tags)
    }
  },
  actions
})
