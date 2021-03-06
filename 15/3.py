import sqlite3

file = open('university.db', 'w')
file.close()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students
(id INTEGER, facultyId INTEGER, name CHAR(50))
""")

cursor.execute("""
CREATE TABLE faculty
(id INTEGER, name CHAR(50))
""")

faculty = ("Математический", "Гуманитарный", "Экономический")
students = ("Иванов Иван", "Петров Петр", "Сидоров Сергей", "Петрова Лидия", "Иванова Елена")

i = 0
for item in faculty:
    i += 1
    cursor.execute("""
        INSERT INTO faculty
        VALUES(?,?)""", (i, item))

cursor.execute("""
    INSERT INTO students
    VALUES(?,?,?)""", (1, 1, students[0]))
cursor.execute("""
    INSERT INTO students
    VALUES(?,?,?)""", (2, 1, students[1]))
cursor.execute("""
    INSERT INTO students
    VALUES(?,?,?)""", (3, 2, students[2]))
cursor.execute("""
    INSERT INTO students
    VALUES(?,?,?)""", (4, 2, students[3]))
cursor.execute("""
    INSERT INTO students
    VALUES(?,?,?)""", (5, 3, students[4]))

print("Студенты по факультетам:")
cursor.execute("""
SELECT students.name, faculty.name
FROM students
LEFT JOIN faculty 
ON students.facultyId = faculty.id
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1])

print("")
print("Количество студентов на каждом факультете:")
cursor.execute("""
SELECT faculty.name, COUNT(students.name)
FROM students
LEFT JOIN faculty 
ON students.facultyId = faculty.id
GROUP BY faculty.name
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1])

print("")
print("Количество студентов на каждом факультете с перечнем кто на каком:")
# В этом запросе используется оператор UNION, который мы ещё не изучали
# Оператор UNION добавляет в список строк одного запроса список строк другого запроса
# При этом у запросов должно быть одинаковое количество полей
# И в конце запроса, благодаря ORDER BY объединенные строки выстраиваются как нам нужно
cursor.execute("""
SELECT COUNT(students.name), faculty.name
FROM students
LEFT JOIN faculty 
ON students.facultyId = faculty.id
GROUP BY faculty.name
UNION
SELECT faculty.name, students.name
FROM students
LEFT JOIN faculty 
ON students.facultyId = faculty.id
ORDER BY faculty.name
""")
cur = cursor.fetchall()
for item in cur:
    print(item[0], "-", item[1])
