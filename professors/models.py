from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class University(models.Model):
    name = models.CharField('Название', max_length=150)
    slug = models.SlugField('Сслылка', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'

class Subject(models.Model):
    name = models.CharField('Название',max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Professor(models.Model):
    full_name = models.CharField('ФИО', max_length=150)
    birth_date = models.DateField('Дата рождения')
    is_checked = models.BooleanField('Проверен?', default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Профессор'
        verbose_name_plural = 'Профессора'
    
class ProfessorRate(models.Model):
    rate = models.PositiveIntegerField(
        'Рейтинг',
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rate)

    class Meta:
        verbose_name = 'Рейтинг профессора'
        verbose_name_plural = 'Рейтинги профессоров'

class ProfessorStory(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    text = models.TextField('Байка о профессоре')

    class Meta:
        verbose_name = 'История о профессоре'
        verbose_name_plural = 'Истории о профессорах'

class SubjectRate(models.Model):
    rate = models.PositiveIntegerField(
        'Рейтинг',
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rate)

    class Meta:
        verbose_name = 'Рейтинг предмета'
        verbose_name_plural = 'Рейтинги предметов'