from django.contrib import admin
from .models import Exam, Requirement, PrepareSource, RequirementVote, PrepareSourceVote


admin.site.register(Exam)
admin.site.register(Requirement)
admin.site.register(PrepareSource)
admin.site.register(RequirementVote)
admin.site.register(PrepareSourceVote)