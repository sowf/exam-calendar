from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class University(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'

class Professor(models.Model):
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    is_checked = models.BooleanField(default=False)
    # subject = models.ForeignKey()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    
class ProfessorRate(models.Model):
    rate = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
