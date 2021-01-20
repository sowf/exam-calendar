from django.contrib import admin
from .models import University, Subject, Professor, ProfessorRate, ProfessorStory,\
    ProfessorVote, StoryVote, SubjectRate


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(University, UniversityAdmin)
admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(ProfessorRate)
admin.site.register(ProfessorStory)
admin.site.register(ProfessorVote)
admin.site.register(StoryVote)
admin.site.register(SubjectRate)