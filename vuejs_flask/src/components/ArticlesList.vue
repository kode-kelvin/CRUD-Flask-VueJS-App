<template>
  <div class="article">
    <div class="shadow bg-body rounded" v-for="post in articles" :key="post.id"
      >{{ post.title }}
      <div class="card-footer mt-4">
        <router-link :to="{ name: 'article_details', params: { id: post.id } }"
          >Read More</router-link
        >
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      articles: [],
    };
  },

  created() {
    axios
      .get("http://127.0.0.1:5000/ape_blog/api/v1.0/articles")
      .then((response) => {
        this.articles = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
<style>
.shadow {
  width: 24rem;
  margin-top: 30px;
  height: 7rem;
}
.shadow:hover {
  border: 3px solid #2196f3;
  width: 30rem;
}
.shadow a {
  text-decoration: none;
}
.article {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  align-content: center;
  flex-direction: row;
  flex-flow: row wrap;
}
</style>
