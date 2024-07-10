const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('mydb.sqlite');

// Create a table
db.serialize(() => {
  db.run('CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)');
});

// Insert data
const stmt = db.prepare('INSERT INTO users VALUES (?, ?)');
stmt.run(1, 'Alice');
stmt.run(2, 'Bob');
stmt.finalize();

console.log("trhrth"+db.each('SELECT * FROM users'))

// Query data
db.each('SELECT id, name FROM users', (err, row) => {
  if (err) console.error(err.message);
  console.log(`${row.id} - ${row.name}`);
});

// Close the database connection
db.close();
