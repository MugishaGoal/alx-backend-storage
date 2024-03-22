-- Create table users with specified attributes

CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(250) NOT NULL UNIQUE,
	name VARCHAR(250)
);
