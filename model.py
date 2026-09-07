from django.db import models
from django.conf import settings

# Existing Course/Lesson models are assumed to be defined above

class Question(models.Model):
    # Relates a question to a specific lesson
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)

    def _str_(self):
        return self.question_text


class Choice(models.Model):
    # Relates multiple choices to one question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def _str_(self):
        return self.choice_text


class Submission(models.Model):
    # Records a user's submitted choices for grading
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - {self.date_submitted}"
