from django.db import models
from users.models import CustomUser as User

class Criteria(models.Model):
    name = models.TextField(max_length=1000)
    arabic_name = models.TextField(max_length=1001)
    Good = 'G'
    Bad = 'B'
    CRITERIA_CATEGORY_CHOICES = [
        (Good, 'G'),
        (Bad, 'B'),
    ]
    criteria_category =  models.CharField(
        max_length = 1 ,
        choices= CRITERIA_CATEGORY_CHOICES,
        default=Good,
    )
    suggested_score = models.IntegerField()
    created_at = models.DateTimeField()
    def __str__(self):
        return str(self.name)

class Evaluation(models.Model):
    parent = models.IntegerField(null=True)
    child = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)
    criteria =  models.ForeignKey(Criteria, on_delete=models.DO_NOTHING)
    Good = 'G'
    Bad = 'B'
    CRITERIA_CATEGORY_CHOICES = [
        (Good, 'G'),
        (Bad, 'B'),
    ]
    criteria_category =  models.CharField(
        max_length = 1 ,
        choices= CRITERIA_CATEGORY_CHOICES,
        default=Good,
    )
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.criteria_name)


