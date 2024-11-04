const express = require("express");
const router = express.Router();

// Sabit kullanıcı bilgileri
const user = {
  username: "eslem",
  password: "99",
};

router.get("/login", (req, res) => {
  res.render("login", { title: "Giriş Yap", error: null });
});

router.post("/login", (req, res) => {
  const { username, password } = req.body;
  if (username === user.username && password === user.password) {
    req.session.loggedIn = true;
    res.redirect("/"); //BURASI index.js'e tekabül ediyor. Ana sayfa
  } else {
    res.render("login", {
      title: "Giriş Yap",
      error: "Geçersiz kullanıcı adı veya şifre",
    });
  }
});

router.get("/logout", (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.redirect("/");
    }
    res.redirect("/auth/login");
  });
});

module.exports = router; //MODÜL HALİNE GETİRDİM DIŞARI EXPORT ETTİM.
