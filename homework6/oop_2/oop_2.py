from datetime import datetime, timedelta
from collections import defaultdict


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self):
        date_now = datetime.now()
        return self.created + self.deadline > date_now


class DeadlineError(Exception):
    pass


class InvalidObject(Exception):
    pass


class Student:

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework, text):
        if homework.is_active():
            return HomeworkResult(self, homework, text)  # HomeworkResult
        else:
            raise DeadlineError('You are late')


class HomeworkResult:
    def __init__(self, author: Student, homework: Homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.now()
        if not isinstance(self.homework, Homework):
            raise InvalidObject('You gave a not Homework object')


class Teacher(Student):
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, days_until_deadline):
        return Homework(text, days_until_deadline)

    @staticmethod
    def check_homework(homework_result: HomeworkResult):

        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework] = homework_result
            return True
        else:
            return False


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
