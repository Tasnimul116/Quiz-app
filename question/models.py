from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=150)

    def __str__ (self):
        return self.course_name
    

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    answer = models.IntegerField()
    question = models.CharField(max_length=150)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)

    def __str__ (self):
        return self.question