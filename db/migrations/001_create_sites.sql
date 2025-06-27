CREATE TABLE IF NOT EXISTS sites (
    id SERIAL PRIMARY KEY,
    site_id TEXT UNIQUE,
    name TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
