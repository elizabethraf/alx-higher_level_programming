-- creates the MySQL server user user_0d_1. 
CREATE USER IF NOT EXISTS user_0d_1@locahost IDENTIFIED BY user_0d_1_pwd;
-- grant previlleges
GRANTS ALL PRIVILEGES ON *.* TO user_0d_1 @localhost;
-- flush
FLUSH PRIVILEGES;

