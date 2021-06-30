var http = require("http");

var count = 0; 

var server = http.createServer(
    ( req, res ) => {
        res.statusCode = 200;
        res.setHeader("content-Type", "text/plain");
        count++;
        res.end("Hello web browser! You are visitor: " + count.toString());
    }
);

server.listen( 8000 );