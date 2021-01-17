from django.db import models
from django.contrib.auth.models import User
from professors.models import Subject, Professor


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предметы')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Профессор')
    date = models.DateField('Дата экзамена')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

class Requirement(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Экзамен')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.CharField('Текст требования', max_length=150)
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'

class PrepareSource(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Экзамен')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')    
    name = models.CharField('Название', max_length=150)
    url = models.URLField('Ссылка', blank=True)
    text = models.TextField('Текст', blank=True)
    document = models.FileField('Файл', blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Источник подготовки'
        verbose_name_plural = 'Источники подготовки'

class PrepareSourceVote(models.Model):
    prepare_source = models.ForeignKey(PrepareSource, on_delete=models.CASCADE, verbose_name='Источник')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    down = models.BooleanField('Вверх?')
    up = models.BooleanField('Вниз?')

    class Meta:
        verbose_name = 'Голос за источник'
        verbose_name_plural = 'Голоса за источники'

class RequirementVote(models.Model):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, verbose_name='Требование')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    down = models.BooleanField('Вверх?')
    up = models.BooleanField('Вниз?')

    class Meta:
        verbose_name = 'Голос за требование'
        verbose_name_plural = 'Голоса за требования'