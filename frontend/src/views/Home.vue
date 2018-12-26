<template>
  <Layout>
    <Layout>
      <Sider>
        <NewsMenu></NewsMenu>
      </Sider>
      <Header></Header>
      <Content></Content>
      <Footer></Footer>
    </Layout>
  </Layout>
</template>

<script>
import newsMenu from '../components/newsMenu'

export default {
  name: 'Home',
  components: {
    'NewsMenu': newsMenu
  }
}
</script>

<style scoped>

</style>
