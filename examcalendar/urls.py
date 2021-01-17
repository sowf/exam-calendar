from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from professors.views import UniversityList, ProfessorListCreate,\
   ProfessorRateCreate, SubjectList, ProfessorStoryListCreate,\
   SubjectRateCreate

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
# Documentation
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

# Admin
   path('admin/', admin.site.urls),

# Professors
   path('api/universities/', UniversityList.as_view()),
   path('api/subjects/', SubjectList.as_view()),
   path('api/subjects/<int:pk>/rate/', SubjectRateCreate.as_view()),
   path('api/professors/<slug:slug>/', ProfessorListCreate.as_view()),
   path('api/professors/<int:pk>/rate/', ProfessorRateCreate.as_view()),
   path('api/professors/<int:pk>/stories/', ProfessorStoryListCreate.as_view()),
   path('api/story/<int:pk>/', ProfessorStoryListCreate.as_view()),

# Exams
]
