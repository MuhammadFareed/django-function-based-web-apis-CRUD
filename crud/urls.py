from django.contrib import admin
from django.urls import path
from api.views import get_students, create_student, update_student, delete_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_students/', get_students),
    path('create_student/', create_student),
    path('update_student/', update_student),
    path('delete_student/', delete_student),
]
