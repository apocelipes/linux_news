import axios from 'axios'

export default {
  // fetch origins and also fetch their tags
  async fetchOrigins ({ commit }) {
    let originResp = await axios.get('http://localhost:8000/origins/')
    for (let origin of originResp.data) {
      commit({
        type: 'addOrigin',
        originName: origin['origin_name'],
        feedLink: origin['feed_link']
      })
      // fetch tags
      let originName = origin['origin_name']
      let tagResp = await axios.get('http://localhost:8000/tags/' + originName + '/')
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
