<template>
  <div class="container form">
    <h4>Update post {{ currentArticle.id }}</h4>
    <form @submit.prevent="updateSelectedArticle">
      <input
        type="text"
        placeholder="enter article title"
        class="form-control"
        v-model="currentArticle.title"
      />
      <br />

      <textarea
        placeholder="enter article body"
        cols="80"
        rows="10"
        class="form-control"
        v-model="currentArticle.body"
      ></textarea>
      <br />
      <button type="submit" class="d-grid gap-2 col-6 mx-auto btn btn-dark"
        >Update</button
      >
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      currentArticle: [],
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    selectedArticle() {
      axios
        .get(`http://127.0.0.1:5000/ape_blog/api/v1.0/article/${this.id}/`)
        .then((response) => {
          this.currentArticle = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateSelectedArticle() {
      axios
        .put(`http://127.0.0.1:5000/ape_blog/api/v1.0/article/${this.id}/`, {
          title: this.currentArticle.title,
          body: this.currentArticle.body,
        })
        .then((response) => {
          console.log(response);
          this.$router.push({ name: "article" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  //calling
  created() {
    this.selectedArticle();
  },
};
</script>

<style></style>
