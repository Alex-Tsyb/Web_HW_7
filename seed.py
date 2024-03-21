from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime, timedelta
import random

# Підключення до бази даних
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізуємо Faker
fake = Faker()

# Додаємо групи
groups = ['A', 'B', 'C']
for name in groups:
    group = Group(name=name)
    session.add(group)

# Додаємо викладачів
teachers = []
for _ in range(random.randint(3, 5)):
    teacher = Teacher(name=fake.name())
    session.add(teacher)
    teachers.append(teacher)

# Додаємо предмети
subjects = []
for _ in range(random.randint(5, 8)):
    subject_name = fake.word()
    teacher = random.choice(teachers)
    subject = Subject(name=subject_name, teacher=teacher)
    session.add(subject)
    subjects.append(subject)

# Додаємо студентів
students = []
for _ in range(random.randint(30, 50)):
    group = session.query(Group).filter_by(name=random.choice(groups)).first()
    student = Student(name=fake.name(), group=group)
    session.add(student)
    students.append(student)

# Додаємо оцінки студентам з усіх предметів
for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            date = datetime.now() - timedelta(days=random.randint(0, 365))
            grade = random.randint(1, 12)
            session.add(Grade(value=grade, date=date, student=student, subject=subject))

# Зберігаємо зміни у базі даних
session.commit()
