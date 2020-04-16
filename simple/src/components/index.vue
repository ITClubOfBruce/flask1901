<template>
  <div class="index-wrapper">
    <div class="index-left">
      <div class="index-left-block all-products">
        <h2>全部产品</h2>
        <template v-for="product in productList">
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list">
              <a v-bind:href="item.url">{{ item.title }}</a>
              <span v-if="item.hot" class="hot-tag">HOT</span>
            </li>
          </ul>
          <hr v-if="!product.last" />
        </template>
      </div>
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li v-for="news in newsList">
            <a v-bind:href="news.url">{{ news.title }}</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="index-right">
      <slider-component></slider-component>
      <div class="index-board-list">
        <div class="index-board-item" v-for="item in boardList">
          <div class="index-board-item-inner">
            <h2>{{ item.title }}</h2>
            <p>{{ item.description }}</p>
            <div class="index-board-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SliderComponent from './sliderComponent'

export default {
  components:{
    SliderComponent
  },
  mounted() {
    axios.get("api/getNewsList")
      .then((response) => {
        // handle success
        console.log(response);
        this.newsList = response.data.list
      })
      .catch((error) => {
        // handle error
        console.log(error);
      });
      axios.get("api/getProductList")
      .then((response) => {
        // handle success
        console.log(response);
        this.productList = response.data
      })
      .catch((error) => {
        // handle error
        console.log(error);
      });
      axios.get("api/getBoardList")
      .then((response) => {
        // handle success
        console.log(response);
        this.boardList = response.data
      })
      .catch((error) => {
        // handle error
        console.log(error);
      });
  },
  data() {
    return {
      newsList: [],
      productList: null,
      boardList:null
    };
  }
};
</script>

<style scoped>
.index-wrapper {
  width: 1200px;
  margin: 0 auto;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-right {
  width: 900px;
  margin-top: 15px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  box-shadow: 0 0 1px #ddd;
  border-radius: 0 0 10px 10px;
}
.index-left-block h2 {
  color: #ffffff;
  background: #4fc08d;
  padding: 10px 15px;
  margin-bottom: 15px;
}
.all-products h3 {
  padding: 0 15px 5px 15px;
  font-weight: bolder;
  color: #222;
}
.index-left-block ul {
  padding: 10px 15px;
}
.index-left-block li {
  padding: 5px;
}
.hot-tag {
  color: white;
  background: purple;
  font-size: 13px;
}
.index-board-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 15px;
}
.index-board-item {
  width: 400px;
  background: #fff;
  box-shadow: 0 0 1px #ddd;
  margin-bottom: 20px;
  padding-top: 20px;
}
.index-board-item-inner {
  height: 125px;
  padding-left: 180px;
  background-image: url(../assets/logo.png);
  background-repeat: no-repeat;
  background-size: 30%;
  background-position: 20px;
}
.index-board-item-inner h2 {
  font-size: 18px;
  font-weight: bolder;
  color: #000000;
  margin-bottom: 15px;
}
.index-board-item-inner p {
  margin-bottom: 15px;
}
.index-board-button {
  width: 80px;
  height: 30px;
  line-height: 30px;
  color: #fff;
  background: limegreen;
  border-radius: 5px;
  text-align: center;
}
</style>