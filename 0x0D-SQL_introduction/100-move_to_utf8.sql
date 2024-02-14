-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field to UTF8
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(258) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;