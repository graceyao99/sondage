from turtle import ondrag
from django.db import models
#le model Question prend en compte deux champs : question et pub_date(qui est la date de publication de la question)
class Question(models.Model):
    question_text = models.CharField(max_length= 200)
    pub_date = models.DateTimeField('date published')


#le model Choice prend en compte deux champs: question_text(le texte du choix) et votes(décompte des votes)
class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        vote = models.IntegerField(default=0)
