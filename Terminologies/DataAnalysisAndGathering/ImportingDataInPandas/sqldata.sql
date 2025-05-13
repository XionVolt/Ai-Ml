CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    join_date DATE
);

INSERT INTO employees (id, name, age, department, salary, join_date) VALUES
(1, 'Alice', 28, 'HR', 55000.00, '2021-06-01'),
(2, 'Bob', 35, 'Engineering', 85000.50, '2020-03-15'),
(3, 'Charlie', 30, 'Sales', 60000.00, '2019-09-10'),
(4, 'Diana', 24, 'Marketing', 50000.00, '2022-01-25'),
(5, 'Ethan', 40, 'Finance', 95000.00, '2018-11-05'),
(6, 'Fay', 32, 'Engineering', 88000.75, '2020-12-11'),
(7, 'George', 29, 'HR', 57000.00, '2021-08-19');