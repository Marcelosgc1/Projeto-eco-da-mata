from django.db import models

# Create your models here.
class Review(models.Model):
    person_name = models.CharField(max_length=60)
    phrase = models.TextField()
    class Grade(models.IntegerChoices):
        _1_STAR = 1, 'Very bad'
        _2_STAR = 2, 'Bad'
        _3_STAR = 3, 'Okay'
        _4_STAR = 4, 'Good'
        _5_STAR = 5, 'Very good'
