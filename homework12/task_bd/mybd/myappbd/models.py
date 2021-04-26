from django.db import models
from django.utils import timezone


class Person(models.Model):
    """
    Abstract class from which the Student and Teacher will inherit.
     Attributes:
        first_name - the name of a person;
        last_name - the surname of a person.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Homework(models.Model):
    """
    Class describes an instance of homework.
    Attributes:
        text - text of the homework.
        deadline - time by which homework should be done.
        created - time to create homework.

    """
    text = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        """
        Method to display a fragment of a class when created in the shell.
        """
        return self.text


class Student(Person):
    """Class describes an instance of a student.
       Attributes:
           first_name - the name of a student;
           last_name - the surname of a student.
       """

    def __str__(self):
        return self.last_name


class Teacher(Person):
    """Class describes an instance of a teacher.
       Attributes:
           first_name - the name of a teacher;
           last_name - the surname of a teacher.
       """

    def __str__(self):
        return self.last_name


class HomeworkResult(models.Model):
    """
    Class describes the result of doing homework.
    Attributes:
        author - student class copy.
        homework - homework class copy.
        solution - homework solution.
        created - date and time of creation.

    """
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.solution
