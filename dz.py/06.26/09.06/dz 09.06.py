
# #1

# # Создание таблицы авторов
# CREATE TABLE authors (
#     id INT PRIMARY KEY,
#     first_name VARCHAR(50),
#     last_name VARCHAR(50)
# );

# # Создание таблицы книг
# CREATE TABLE books (
#     id INT PRIMARY KEY,
#     title VARCHAR(100),
#     author_id INT,
#     publication_year INT,
#     FOREIGN KEY (author_id) REFERENCES authors(id)
# );

# # Создание таблицы продаж
# CREATE TABLE sales (
#     id INT PRIMARY KEY,
#     book_id INT,
#     quantity INT,
#     FOREIGN KEY (book_id) REFERENCES books(id)
# );

# # Заполнение таблицы авторов
# INSERT INTO authors (id, first_name, last_name) VALUES
# (1, 'Александр', 'Пушкин'),
# (2, 'Лев', 'Толстой'),
# (3, 'Федор', 'Достоевский'),
# (4, 'Марк', 'Твен'); -- Автор без книг для проверки LEFT JOIN

# # Заполнение таблицы книг
# INSERT INTO books (id, title, author_id, publication_year) VALUES
# (101, 'Евгений Онегин', 1, 1833),
# (102, 'Капитанская дочка', 1, 1836),
# (103, 'Война и мир', 2, 1869),
# (104, 'Преступление и наказание', 3, 1866),
# (105, 'Книга без автора', NULL, 2026); -- Книга без автора для проверки RIGHT JOIN

# # Заполнение таблицы продаж
# INSERT INTO sales (id, book_id, quantity) VALUES
# (1, 101, 10),
# (2, 101, 5),
# (3, 102, 20),
# (4, 103, 7),
# (5, 104, 12);




# # 2

# # INNER JOIN: только книги, у которых есть авторы
# SELECT b.title, a.first_name, a.last_name
# FROM books b
# INNER JOIN authors a ON b.author_id = a.id;

# # LEFT JOIN: все авторы, даже если у них нет книг
# SELECT a.first_name, a.last_name, b.title
# FROM authors a
# LEFT JOIN books b ON a.id = b.author_id;

# #  RIGHT JOIN: все книги, даже если автор не указан
# SELECT b.title, a.first_name, a.last_name
# FROM authors a
# RIGHT JOIN books b ON a.id = b.author_id;




# # 3
# # INNER JOIN: только те книги, которые имеют автора И были проданы
# SELECT a.first_name, a.last_name, b.title, s.quantity
# FROM authors a
# INNER JOIN books b ON a.id = b.author_id
# INNER JOIN sales s ON b.id = s.book_id;

# #LEFT JOIN: абсолютно все авторы, их книги и продажи (включая пустые значения)
# SELECT a.first_name, a.last_name, b.title, s.quantity
# FROM authors a
# LEFT JOIN books b ON a.id = b.author_id
# LEFT JOIN sales s ON b.id = s.book_id;





# # 4
# #INNER JOIN: общее количество продаж по авторам 
# SELECT a.first_name, a.last_name, SUM(s.quantity) AS total_sold
# FROM authors a
# INNER JOIN books b ON a.id = b.author_id
# INNER JOIN sales s ON b.id = s.book_id
# GROUP BY a.id, a.first_name, a.last_name;

# #LEFT JOIN: общее количество продаж для всех авторов 
# SELECT a.first_name, a.last_name, COALESCE(SUM(s.quantity), 0) AS total_sold
# FROM authors a
# LEFT JOIN books b ON a.id = b.author_id
# LEFT JOIN sales s ON b.id = s.book_id
# GROUP BY a.id, a.first_name, a.last_name;





# # 5
# # Автор с наибольшим количеством проданных книг
# SELECT a.first_name, a.last_name, SUM(s.quantity) AS total_sold
# FROM authors a
# INNER JOIN books b ON a.id = b.author_id
# INNER JOIN sales s ON b.id = s.book_id
# GROUP BY a.id, a.first_name, a.last_name
# HAVING SUM(s.quantity) = (
#     -- Подзапрос находит максимальное суммарное количество продаж среди всех авторов
#     SELECT MAX(author_sales.total)
#     FROM (
#         SELECT SUM(s2.quantity) AS total
#         FROM books b2
#         INNER JOIN sales s2 ON b2.id = s2.book_id
#         GROUP BY b2.author_id
#     ) AS author_sales
# );

# # Книги, продажи которых выше среднего количества продаж всех книг
# SELECT b.title, SUM(s.quantity) AS book_sales
# FROM books b
# INNER JOIN sales s ON b.id = s.book_id
# GROUP BY b.id, b.title
# HAVING SUM(s.quantity) > (
#     -- Подзапрос считает среднее арифметическое продаж по всем книгам
#     SELECT AVG(book_total_sales.total)
#     FROM (
#         SELECT SUM(quantity) AS total
#         FROM sales
#         GROUP BY book_id
#     ) AS book_total_sales
# );
