-- Script that creates user_0d_1 with all priviledges
-- With password 'user_0d_1_pwd'
-- Should suport if user still exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
