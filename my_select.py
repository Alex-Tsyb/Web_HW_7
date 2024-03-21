
from sqlalchemy import func
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()
# Введи імя предмету
subject_name = "various"
group_name = "A"
teacher_name = "Ashley Thompson"
student_name = "Ryan Greene"

def select_1(session):
    query = session.query(Student.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                   .join(Grade, Student.id == Grade.student_id) \
                   .group_by(Student.id) \
                   .order_by(desc('avg_grade')) \
                   .limit(5)

    result = query.all()
    return result

def select_2(session, subject_name):
    query = session.query(Student.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                   .join(Grade, Student.id == Grade.student_id) \
                   .join(Subject, Grade.subject_id == Subject.id) \
                   .filter(Subject.name == subject_name) \
                   .group_by(Student.id) \
                   .order_by(desc('avg_grade')) \
                   .first()

    result = query
    return result

def select_3(session, subject_name):
    query = session.query(Group.name, func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                   .join(Student, Group.id == Student.group_id) \
                   .join(Grade, Student.id == Grade.student_id) \
                   .join(Subject, Grade.subject_id == Subject.id) \
                   .filter(Subject.name == subject_name) \
                   .group_by(Group.id)

    result = query.all()
    return result

def select_4(session):
    query = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade'))

    result = query.scalar()
    return result

def select_5(session, teacher_name):
    query = session.query(Subject.name) \
                   .join(Teacher, Subject.teacher_id == Teacher.id) \
                   .filter(Teacher.name == teacher_name)

    result = query.all()
    return result

def select_6(session, group_name):
    query = session.query(Student.name) \
                   .join(Group, Student.group_id == Group.id) \
                   .filter(Group.name == group_name)

    result = query.all()
    return result

def select_7(session, group_name, subject_name):
    query = session.query(Student.name, Grade.value) \
                   .join(Group, Student.group_id == Group.id) \
                   .join(Grade, Student.id == Grade.student_id) \
                   .join(Subject, Grade.subject_id == Subject.id) \
                   .filter(Group.name == group_name) \
                   .filter(Subject.name == subject_name)

    result = query.all()
    return result

def select_8(session, teacher_name):
    query = session.query(func.round(func.avg(Grade.value), 2).label('avg_grade')) \
                   .join(Subject, Grade.subject_id == Subject.id) \
                   .join(Teacher, Subject.teacher_id == Teacher.id) \
                   .filter(Teacher.name == teacher_name)

    result = query.scalar()
    return result

def select_9(session, student_name):
    query = session.query(func.distinct(Subject.name)) \
                   .join(Grade, Subject.id == Grade.subject_id) \
                   .join(Student, Grade.student_id == Student.id) \
                   .filter(Student.name == student_name)

    result = query.all()
    return result

def select_10(session, student_name, teacher_name):
    query = session.query(func.distinct(Subject.name)) \
                   .join(Grade, Subject.id == Grade.subject_id) \
                   .join(Student, Grade.student_id == Student.id) \
                   .join(Teacher, Subject.teacher_id == Teacher.id) \
                   .filter(Student.name == student_name) \
                   .filter(Teacher.name == teacher_name)
    
    result = query.all()
    return result


# Виклик функцій із базою даних
result_1 = select_1(session)
print("Task 1")
print(result_1)

result_2 = select_2(session, subject_name)
print("\nTask 2")
print(result_2)

result_3 = select_3(session, subject_name)
print("\nTask 3")
print(result_3)

result_4 = select_4(session)
print("\nTask 4")
print(result_4)

result_5 = select_5(session, teacher_name)
print("\nTask 5")
print(result_5)

result_6 = select_6(session, group_name)
print("\nTask 6")
print(result_6)

result_7 = select_7(session, group_name, subject_name)
print("\nTask 7")
print(result_7)

result_8 = select_8(session, teacher_name)
print("\nTask 8")
print(result_8)

result_9 = select_9(session, student_name)
print("\nTask 9")
print(result_9)

result_10 = select_10(session, student_name, teacher_name)
print("\nTask 10")
print(result_10)

session.close()
 