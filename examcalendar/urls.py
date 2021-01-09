from django.contrib import admin
from django.urls import path
from professors.views import UniversityList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/universities/', UniversityList.as_view()),
]
