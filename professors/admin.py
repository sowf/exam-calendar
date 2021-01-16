from django.contrib import admin
from .models import University, Professor, ProfessorRate


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(University, UniversityAdmin)
admin.site.register(Professor)
admin.site.register(ProfessorRate)