export default{
    install:function(Vue){
        // 平方
        Vue.directive('square',function(el,binding){
            el.innerHTML = Math.pow(binding.value,2)
        });
        // 开方
        Vue.directive('sqrt',function(el,binding){
            el.innerHTML = Math.sqrt(binding.value)
        })
        // 把item当做角度，计算sin，cos，tan 值
    }
}