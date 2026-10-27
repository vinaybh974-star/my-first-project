
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
);

INSERT OR IGNORE INTO students (id, name, age, course)
VALUES
    (1, 'Ravi', 20, 'Python'),
    (2, 'Priya', 22, 'SQL'),
    (3, 'Amit', 21, 'Data Analytics');

SELECT * FROM students;
