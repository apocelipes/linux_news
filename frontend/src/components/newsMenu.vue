<template>
  <Menu theme="dark">
    <Submenu v-for="(origin, index) of origins" :name="origin.originName" :key="index">
      <template slot="title">{{origin.originName}}</template>
      <MenuGroup title="分类">
        <MenuItem v-for="tag of originTags[origin.originName]" :name="origin.originName+'-'+tag" :key="tag">
          {{tag}}
        </MenuItem>
      </MenuGroup>
    </Submenu>
  </Menu>
</template>

<script>
export default {
  name: 'newsMenu',
  data () {
    return {
    }
  },
  computed: {
    origins () {
      if (this.$store.state.origins.length === 0) {
        this.$store.dispatch('fetchOrigins')
      }
      return this.$store.state.origins
    },
    originTags () {
      return this.$store.state.originTags
    }
  }
}
</script>

<style scoped>
</style>
