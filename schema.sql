CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_id TEXT NOT NULL UNIQUE
);
