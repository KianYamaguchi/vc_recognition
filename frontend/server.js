const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// EJSをテンプレートエンジンとして設定
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// 静的ファイルの提供
app.use(express.static(path.join(__dirname, "public")));

// メインページのルート
app.get("/", (req, res) => {
    res.render("index");
});

// サーバーを起動
app.listen(PORT, () => {
    console.log(`フロントエンドサーバーが http://127.0.0.1:${PORT} で動作しています`);
});