import random
import sqlite3
from faker import Faker

fake = Faker()

# Підключення до бази даних SQLite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

# Створення таблиць
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);
""")

cursor.execute("""
CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    name TEXT
);
""")

cursor.execute("""
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name TEXT
);
""")

cursor.execute("""
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    teacher_id INTEGER
);
""")

cursor.execute("""
CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date DATE
);
""")

# Заповнення таблиць випадковими даними
num_students = random.randint(30, 50)
num_groups = 3
num_subjects = random.randint(5, 8)
num_teachers = random.randint(3, 5)
num_grades_per_student = random.randint(15, 20)

# Додавання груп
for i in range(num_groups):
    group_name = f"Group {i + 1}"
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))

# Додавання студентів
for i in range(num_students):
    student_name = fake.name()
    group_id = random.randint(1, num_groups)
    cursor.execute(
        "INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))

# Додавання викладачів
for i in range(num_teachers):
    teacher_name = fake.name()
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

# Додавання предметів з вказанням викладача
for i in range(num_subjects):
    subject_name = f"Subject {i + 1}"
    teacher_id = random.randint(1, num_teachers)
    cursor.execute(
        "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, teacher_id))

# Додавання оцінок
for student_id in range(1, num_students + 1):
    for subject_id in range(1, num_subjects + 1):
        for _ in range(num_grades_per_student):
            grade = random.randint(1, 5)
            date = fake.date_between(start_date='-6M', end_date='today')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date))

# Збереження змін та закриття з'єднання
connection.commit()
cursor.close()
connection.close()
