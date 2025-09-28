-- ----------------------------------------
-- Drop tables if they exist
-- ----------------------------------------
DROP TABLE IF EXISTS books_authors;
DROP TABLE IF EXISTS borrowings;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS categories;

-- ----------------------------------------
-- Create tables
-- ----------------------------------------
-- Categories table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Authors table
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    biography TEXT,
    birth_year INT
);

-- Books table
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    publication_year INT,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL
);

-- Many-to-Many relationship table
CREATE TABLE books_authors (
    book_id INT REFERENCES books(id) ON DELETE CASCADE,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE,
    PRIMARY KEY (book_id, author_id)
);

-- Borrowings table (optional)
CREATE TABLE borrowings (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id) ON DELETE CASCADE,
    borrower_name VARCHAR(100) NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE
);

-- ----------------------------------------
-- Insert seed data
-- ----------------------------------------
-- Categories
INSERT INTO categories (name, description) VALUES
('Fiction', 'روايات وقصص خيالية'),
('Science', 'كتب علمية وتقنية'),
('History', 'كتب تاريخية'),
('Biography', 'سير ذاتية'),
('Fantasy', 'خيال وفانتازيا');

-- Authors
INSERT INTO authors (name, biography, birth_year) VALUES
('J.K. Rowling', 'Author of Harry Potter series', 1965),
('George Orwell', 'Author of 1984 and Animal Farm', 1903),
('Yuval Noah Harari', 'Author of Sapiens', 1976),
('Isaac Asimov', 'Science fiction author', 1920),
('Agatha Christie', 'Famous mystery writer', 1890),
('J.R.R. Tolkien', 'Author of Lord of the Rings', 1892),
('Stephen Hawking', 'Famous physicist and author', 1942),
('Leo Tolstoy', 'Russian novelist', 1828),
('Mark Twain', 'American author', 1835),
('Ernest Hemingway', 'American novelist', 1899);

-- Books
INSERT INTO books (title, description, publication_year, category_id) VALUES
('Harry Potter and the Sorcerer''s Stone', 'Fantasy book about a young wizard', 1997, 5),
('1984', 'Dystopian novel', 1949, 1),
('Sapiens', 'A brief history of humankind', 2011, 2),
('Foundation', 'Science fiction series', 1951, 2),
('Murder on the Orient Express', 'Detective novel', 1934, 1),
('The Lord of the Rings', 'Epic fantasy novel', 1954, 5),
('A Brief History of Time', 'Cosmology book', 1988, 2),
('War and Peace', 'Russian historical novel', 1869, 3),
('Adventures of Huckleberry Finn', 'American classic novel', 1884, 1),
('The Old Man and the Sea', 'Short novel', 1952, 1);

-- books_authors relationships
INSERT INTO books_authors (book_id, author_id) VALUES
(1, 1), -- Harry Potter → J.K. Rowling
(2, 2), -- 1984 → George Orwell
(3, 3), -- Sapiens → Yuval Noah Harari
(4, 4), -- Foundation → Isaac Asimov
(5, 5), -- Murder on the Orient Express → Agatha Christie
(6, 6), -- Lord of the Rings → J.R.R. Tolkien
(7, 7), -- A Brief History of Time → Stephen Hawking
(8, 8), -- War and Peace → Leo Tolstoy
(9, 9), -- Huckleberry Finn → Mark Twain
(10, 10); -- The Old Man and the Sea → Ernest Hemingway





SELECT * FROM books;