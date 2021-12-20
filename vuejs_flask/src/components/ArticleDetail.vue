<template>
  <div class="contain">
    <h2>{{ article.date }}</h2>
    <h1>{{ article.title }}</h1>
    <p class="gradient_select">{{ article.body }}</p>
    <div class="btn-group" role="group" aria-label="Basic mixed styles example">
      <button type="button" class="btn btn-danger" @click="deleteArticle"
        >Delete</button
      >

      <router-link
        class="btn btn-primary"
        :to="{ name: 'update_article', params: { id: article.id } }"
        >Update</router-link
      >
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      article: [],
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    //   get article
    articleDetail() {
      axios
        .get(`http://127.0.0.1:5000/ape_blog/api/v1.0/article/${this.id}/`)
        .then((response) => {
          this.article = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // delete article
    deleteArticle() {
      axios
        .delete(`http://127.0.0.1:5000/ape_blog/api/v1.0/article/${this.id}/`)
        .then(() => {
          this.$router.push({ name: "article" }).catch((error) => {
            console.log(error);
          });
        });
    },
  },
  created() {
    this.articleDetail();
  },
};
</script>
<style>
html,
body {
  position: relative;
}

.contain {
  max-width: 40em;
  margin: 0 auto;
  margin-top: 50px;
}

h2 {
  position: relative;
  font-size: 0.875em;
  font-weight: 700;
  text-transform: uppercase;
  font-family: "open-sans", sans-serif;
  color: #cb2953;
  letter-spacing: 0.35em;
}

h1 {
  font-size: 2.5em;
  font-weight: 300;
  font-family: "bookmania", serif;
}

p {
  font-weight: 300;
  line-height: 2em;
  font-family: "open-sans", sans-serif;
}
</style>
