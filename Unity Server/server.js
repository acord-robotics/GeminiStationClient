// Entry point for the application

var express = require("express");

var app = express();

app.get("/", (req, res) => {
    res.send("Hello world!")
});

app.get("/users/:id", (req, res) => {
    
    var Data = {
        "userid": req.params["id"],
        "username": "quill18",
        "wins": 18,
        "losses": 1000
    };

    res.json(Data.username);
});

app.listen( 8000, () => {
    console.log("Server has started")
});