<template>
  <div>
    <h1 class="">{{ msg }}</h1>
    <div class="app-header">
      <Header/>
    </div>
    <div class="app-content">
      <Content/>
    </div>
    <div class="app-footer">
      <Footer/>
    </div>
  </div>
</template>

<script>
import Header from './components/Header'
import Content from './components/Content'
import Footer from './components/Footer'
export default {
  data() {
    return {
      msg:'基础模板'
    };
  },
  components:{
    Header,
    Content,
    Footer
  }
};
</script>

<style scoped>
h1{
  color: red;
}
</style>
