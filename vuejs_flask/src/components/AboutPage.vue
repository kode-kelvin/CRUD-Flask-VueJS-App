<template>
  <div class="section">
    <div class="containers">
      <div class="content-section">
        <div class="title">
          <h1>Flask & VueJS CRUD APP</h1>
        </div>
        <div class="content">
          <h3>This project is a basic CRUD App using Flask and VueJS</h3>
          <p
            >In this project, we built a simple CRUD app using VueJS in Frontend
            and Flask as our BackEnd technology.</p
          >
          <p
            >Flask - to build our API / VueJS - for our Frontend / Axios - for
            our API calls</p
          >

          <div class="button">
            <a
              href="https://github.com/kode-kelvin/Flask-VueJS-CRUD-APP"
              target="_blank"
              rel="noopener"
              >Source Code</a
            >
          </div>
        </div>
        <div class="social">
          <a
            href="https://www.linkedin.com/in/kelvin-obed-565877171/"
            target="_blank"
            rel="noopener"
            ><i class="fab fa-linkedin"></i
          ></a>
          <a
            href="https://github.com/kode-kelvin"
            rel="noopener"
            target="_blank"
            ><i class="fab fa-github"></i
          ></a>
        </div>
      </div>
      <div class="image-section">
        <img :src="logo" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data: () => ({
    logo: require("@/assets/flaskyvuejs.jpg"),
  }),
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400&display=swap");
@import url("https://pro.fontawesome.com/releases/v5.10.0/css/all.css");
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.section {
  width: 100%;
  min-height: 100vh;
}
.containers {
  width: 80%;
  display: block;
  margin: auto;
  padding-top: 100px;
}
.content-section {
  float: left;
  width: 55%;
}
.image-section {
  float: right;
  width: 40%;
}
.image-section img {
  width: 100%;
  height: auto;
}
.content-section .title {
  text-transform: uppercase;
  font-size: 28px;
}
.content-section .content h3 {
  margin-top: 20px;
  color: #5d5d5d;
  font-size: 21px;
}
.content-section .content p {
  margin-top: 10px;
  font-family: sans-serif;
  font-size: 18px;
  line-height: 1.5;
}
.content-section .content .button {
  margin-top: 30px;
}
.content-section .content .button a {
  background-color: #3d3d3d;
  padding: 12px 40px;
  text-decoration: none;
  color: #fff;
  font-size: 25px;
  letter-spacing: 1.5px;
}
.content-section .content .button a:hover {
  background-color: #2196f3;
  color: #fff;
}
.content-section .social {
  margin: 40px 40px;
}
.content-section .social i {
  color: #2196f3;
  font-size: 30px;
  padding: 0px 10px;
}
.content-section .social i:hover {
  color: #3d3d3d;
}
@media screen and (max-width: 768px) {
  .containers {
    width: 80%;
    display: block;
    margin: auto;
    padding-top: 50px;
  }
  .content-section {
    float: none;
    width: 100%;
    display: block;
    margin: auto;
  }
  .image-section {
    float: none;
    width: 100%;
  }
  .image-section img {
    width: 100%;
    height: auto;
    display: block;
    margin: auto;
  }
  .content-section .title {
    text-align: center;
    font-size: 19px;
  }
  .content-section .content .button {
    text-align: center;
  }
  .content-section .content .button a {
    padding: 9px 30px;
  }
  .content-section .social {
    text-align: center;
  }
}
</style>
