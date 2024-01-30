from django.contrib.auth import get_user_model
from django.db import models

from master_records.models import TestTopic


class Factor(models.Model):
    practice_choices = (
        ("Coding Fundamentals", "CF"), ("Languages", "LG"), ("Specialization", "SZ")
    )

    category = models.CharField(max_length=20, choices=practice_choices)
    topics = models.ForeignKey(TestTopic, models.PROTECT)

    def __str__(self):
        return self.category


class Discussion(models.Model):
    comments = models.TextField()


class Question(models.Model):
    factor = models.ForeignKey(Factor, models.PROTECT)
    problem = models.TextField()
    discussion = models.ManyToOneRel('discussion', Discussion, 'comments')


class Submission(models.Model):
    submitted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    problem = models.ForeignKey(Question, models.PROTECT)
    solution = models.TextField()

    def __str__(self):
        return str(self.submitted_by)
