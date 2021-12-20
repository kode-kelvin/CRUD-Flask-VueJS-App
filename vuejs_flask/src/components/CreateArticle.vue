<template>
  <div class="container form">
    <h4>Create New Article</h4>

    <br />
    <form @submit.prevent="addArticle">
      <input
        type="text"
        placeholder="enter article title"
        v-model="formData.title"
        class="form-control"
      />
      <br />

      <textarea
        placeholder="enter article body"
        cols="80"
        rows="10"
        v-model="formData.body"
        class="form-control"
      ></textarea>
      <br />
      <button type="submit" class="d-grid gap-2 col-6 mx-auto btn btn-dark"
        >create</button
      >
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      formData: {
        title: "",
        body: "",
      },
    };
  },
  methods: {
    addArticle() {
      axios
        .post("http://127.0.0.1:5000/ape_blog/api/v1.0/article", this.formData)
        .then((response) => {
          console.log(response);
          this.$router.push({ name: "article" });
        })
        .catch((error) => {
          console.log(error, error.response);
        });
    },
  },
};
</script>

<style>
.form {
  margin-top: 5rem;
}
</style>
