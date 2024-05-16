// app.js

const express = require('express');
const app = express();
const port = 3000;

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Serve static files from the "public" directory
app.use(express.static('public'));

// Home route
app.get('/', (req, res) => {
    res.render('index', { title: 'Home' });
});

// API route
app.get('/api', (req, res) => {
    res.json({ message: 'Hello, world!' });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
