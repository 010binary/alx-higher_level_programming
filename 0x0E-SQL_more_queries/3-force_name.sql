-- creates the table name_not_null
-- table data: id INT with the default value 1, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);