CREATE DATABASE login_and_registration;

USE login_and_registration;

CREATE TABLE users(
users_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(45) NOT NULL,
last_name VARCHAR(45) NOT NULL,
email VARCHAR(45) NOT NULL,
users_password varchar(255) NOT NULL,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL 
);

INSERT INTO users(users_id,first_name,last_name,email,users_password,created_at,updated_at)
VALUES 
(1, 'Bryan', 'Cascante', 'bcascante@outlook.com', 'pass1234', SYSDATE(), SYSDATE() );



