<template>
<div class="header-content">
<Menu mode="horizontal" theme="dark" active-name="dateOrder">
  <MenuItem title="按日期显示" name="dateOrder">按日期显示</MenuItem>
  <MenuItem title="我的收藏" name="favorite">
    <Icon type="md-star" />
    我的收藏
  </MenuItem>
  <MenuItem title="登录" name="userLogin">
    <Icon type="md-person"/>
    登录
  </MenuItem>
</Menu>
</div>
</template>

<script>
export default {
  name: 'newsHeader'
}
</script>

<style scoped>
.header-content {
  float: right;
}
</style>
