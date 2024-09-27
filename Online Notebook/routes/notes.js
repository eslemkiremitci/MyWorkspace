const express = require("express");
const router = express.Router();

let notes = []; // JSON objelerinde veriler tutulacak

// Tüm notları listeleme
router.get("/", (req, res) => {
  res.render("notes", { title: "Notlar", notes });
});

// Not ekleme formunu gösterme
router.get("/add", (req, res) => {
  res.render("addNote", { title: "Yeni Not Ekle" });
});

// Yeni not ekleme
router.post("/add", (req, res) => {
  const { title, content } = req.body;
  notes.push({ id: notes.length + 1, title, content });
  res.redirect("/notes");
});

// Not düzenleme formunu gösterme
router.get("/edit/:id", (req, res) => {
  const note = notes.find(n => n.id == req.params.id);
  if (note) {
    res.render("editNote", { title: "Notu Düzenle", note });
  } else {
    res.redirect("/notes");
  }
});

// Not düzenleme
router.post("/edit/:id", (req, res) => {
  const { title, content } = req.body;
  const note = notes.find(n => n.id == req.params.id);
  if (note) {
    note.title = title;
    note.content = content;
  }
  res.redirect("/notes");
});

module.exports = router;
