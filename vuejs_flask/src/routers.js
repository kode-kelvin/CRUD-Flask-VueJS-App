import { createRouter, createWebHistory } from "vue-router";
import Article from "./components/ArticlesList";
import CreateArticle from "./components/CreateArticle";
import ArticleDetail from "./components/ArticleDetail";
import UpdateArticle from "./components/UpdateArticle";
import AboutPage from "./components/AboutPage";

const routes = [
  {
    path: "/",
    name: "article",
    component: Article,
  },
  {
    path: "/about_page",
    name: "about",
    component: AboutPage,
  },
  // {
  //   path: "/github",
  //   beforeEnter() {
  //     location.href = "http://github.com";
  //   },
  // },

  {
    path: "/create_article",
    name: "create",
    component: CreateArticle,
  },
  {
    path: "/article_details/:id",
    name: "article_details",
    component: ArticleDetail,
    props: true,
  },
  {
    path: "/update_article/:id",
    name: "update_article",
    component: UpdateArticle,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
