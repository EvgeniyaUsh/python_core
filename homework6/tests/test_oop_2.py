from collections import defaultdict
from datetime import datetime

from homework6.oop_2.oop_2 import Homework, HomeworkResult, Student, Teacher


def test_name_teacher():
    opp_teacher = Teacher("Daniil", "Shadrin")
    assert opp_teacher.first_name == "Daniil"
    assert opp_teacher.last_name == "Shadrin"


def test_name_student():
    lazy_student = Student("Roman", "Petrov")
    assert lazy_student.first_name == "Roman"
    assert lazy_student.last_name == "Petrov"


def test_create_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    assert oop_hw.created == datetime.now()


def test_check_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_teacher_reset_all_results():
    teacher = Teacher("Peter", "Petrov")
    good_student = Student("Lev", "Sokolov")
    homework = Homework("hw1", 1)
    teacher.check_homework(HomeworkResult(good_student, homework, "solution"))
    teacher.reset_results()
    assert teacher.homework_done == defaultdict(set)
