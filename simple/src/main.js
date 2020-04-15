import Vue from 'vue'
import VueRouter from 'vue-router'
import Base from './Base.vue'
import IndexPage from './components/index.vue'

Vue.use(VueRouter)
let router = new VueRouter({
  mode:'history',
  routes:[
    {
      path:'/',
      component:IndexPage
    }
  ]
})

new Vue({
  el: '#app',
  router,
  components:{
    Base
  },
  template:'<Base/>'
})
