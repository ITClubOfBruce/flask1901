<template id='app'></template>

<script>
Vue.component("hello-component", {
  template: "#hello",
  el: function() {
    return "#hello";
  },
  data: function() {
    return {
      msg: "hello"
    };
  }
});
new Vue({
  el: "#app",
  data: {}
});
</script>
<style>
</style>
