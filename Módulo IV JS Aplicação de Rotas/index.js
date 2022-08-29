var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Conectado!');
});

app.listen(3000, function () {
    console.log('Teste de Rota!');
});
