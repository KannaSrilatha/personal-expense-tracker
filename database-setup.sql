CREATE TABLE Expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(50),
    amount DECIMAL(10, 2),
    description TEXT
);