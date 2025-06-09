const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/get-item', (req, res) => {
    res.send('You sent a GET request');
});

app.post('/add-item', (req, res) => {
    const { name, qty } = req.body;
    res.send(`Added ${qty} of ${name}`);
});

app.delete('/delete-item/:itemId', (req, res) => {
    res.send(`Deleted item with ID ${req.params.itemId}`);
});

app.listen(5000, () => console.log('Server running'));
