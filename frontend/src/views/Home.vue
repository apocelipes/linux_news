<template>
  <Layout>
    <Sider class="news-sider">
      <Layout>
        <Header class="sider-header">新闻源</Header>
        <Content>
          <NewsMenu></NewsMenu>
        </Content>
      </Layout>
    </Sider>
    <Layout>
      <Header class="header-bar">
        <NewsHeader></NewsHeader>
      </Header>
      <Content></Content>
      <Footer></Footer>
    </Layout>
  </Layout>
</template>

<script>
import newsMenu from '../components/newsMenu'
import newsHeader from '../components/newsHeader'

export default {
  name: 'Home',
  components: {
    'NewsMenu': newsMenu,
    'NewsHeader': newsHeader
  }
}
</script>

<style scoped>
.sider-header {
  font-size: 30px;
  text-align: center;
  color: white;
}
.news-sider {
  width: 20%;
}
.header-bar {
  width: 100%;
}
</style>
