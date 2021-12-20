<template>
  <nav @click="myFunction">
    <router-link class="navbar-brand" to="/">Blog Ape</router-link>
    <router-link class="navbar-brand" to="/about_page">About</router-link>
    <router-link class="navbar-brand" to="/create_article"
      >Create Article</router-link
    >
  </nav>
</template>

<script>
export default {
  methods: {
    myFunction(e) {
      var elems = document.querySelector(".active");
      if (elems !== null) {
        elems.classList.remove("active");
      }
      e.target.className = "active";
    },
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap");

nav {
  display: flex;
  height: 80px;
  background-color: white;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  font-family: Open Sans;
}

nav a {
  flex: 1;
  text-decoration: none;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  color: black;
  transition: all 0.2s;
}

nav a:hover {
  background: #2196f3;
  color: white;
}

.active {
  border-bottom: 10px solid #2196f3;
  padding-top: 10px;
}

main {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  height: calc(100vh - 80px);
}

h1,
h2 {
  margin: 0;
}

h1 {
  font-size: 3em;
}
</style>
