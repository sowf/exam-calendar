from django.contrib import admin
from .models import University, Subject, Professor, ProfessorRate, ProfessorStory, SubjectRate


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(University, UniversityAdmin)
admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(ProfessorRate)
admin.site.register(ProfessorStory)
admin.site.register(SubjectRate)