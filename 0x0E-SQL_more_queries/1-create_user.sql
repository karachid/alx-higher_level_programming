-- script that creates a new user and assign all privileges on my MySQL server
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost
