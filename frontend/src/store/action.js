import axios from 'axios'
import {
  ORIGINS,
  ORIGIN_TAGS
} from './config'

// set csrf settings
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

export default {
  // fetch origins and also fetch their tags
  async fetchOrigins ({ commit }) {
    let originResp = await axios.get(ORIGINS)
    for (let origin of originResp.data) {
      commit({
        type: 'addOrigin',
        originName: origin['origin_name'],
        feedLink: origin['feed_link']
      })
      // fetch tags
      let originName = origin['origin_name']
      let tagResp = await axios.get(ORIGIN_TAGS + originName + '/')
      let tags = []
      for (let tag of tagResp.data) {
        tags = tags.concat(tag['tag_name'])
      }
      commit({
        type: 'addOriginTags',
        originName,
        tags
      })
    }
  }
}
