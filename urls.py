from django.urls import path
from . import views

urlpatterns = [
    # Paths for submit and show_exam_result functions
    path('submit/', views.submit, name='submit'),
    path('exam-result/', views.show_exam_result, name='show_exam_result'),
]
