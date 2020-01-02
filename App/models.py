from django.db import models


# Create your models here.
class Grade(models.Model):
    grade_name = models.CharField(max_length=32)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    name = models.CharField(max_length=32)
    gender = models.BooleanField(default=True)
    math = models.FloatField(max_length=32)
    s_grade = models.ForeignKey(Grade)

    class Meta:
        db_table = 'student'
