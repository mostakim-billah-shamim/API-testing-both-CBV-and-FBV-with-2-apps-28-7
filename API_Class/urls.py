from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentPage.as_view(), name='student'),
    path('student/<int:id>/', StudentPage.as_view(), name='student_update'),

    path('teacher/', TeacherPage.as_view(), name='teacher'),
    path('teacher/<int:id>/', TeacherPage.as_view(), name='teacher_update'),
]