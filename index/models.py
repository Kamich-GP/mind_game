from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.category_name)


class Question(models.Model):
    question = models.TextField()
    score = models.IntegerField()
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return str(self.question)


class Team(models.Model):
    team_name = models.CharField(max_length=64)
    team_score = models.IntegerField()

    def __str__(self):
        return str(self.team_name)
