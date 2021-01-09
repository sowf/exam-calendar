from django.contrib import admin
from .models import University, Professor, ProfessorRate


admin.site.register(University)
admin.site.register(Professor)
admin.site.register(ProfessorRate)