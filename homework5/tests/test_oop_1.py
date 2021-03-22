from datetime import datetime, timedelta

from homework5.oop.oop_1 import Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")


def test_name_teacher():
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_name_student():
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_create_homework():
    expired_homework = teacher.create_homework("Learn functions", 1)
    assert expired_homework.created == datetime.now()


def test_deadline_0_days():
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert expired_homework.deadline == timedelta(0)


def test_deadline_5_days():
    expired_homework = teacher.create_homework("Smth text", 5)
    assert expired_homework.deadline == timedelta(5)


def test_text_homework():
    expired_homework = teacher.create_homework("Learn functions", 10)
    assert expired_homework.text == "Learn functions"


def test_do_homework_return():
    expired_homework = teacher.create_homework("Smth text", 0)
    assert student.do_homework(expired_homework) is None  # and 'You are late'  ?
