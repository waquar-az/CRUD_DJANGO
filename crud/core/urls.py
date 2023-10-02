from django.urls import path
from .views import Home, Add_Student,Delete_student,Edit_student
urlpatterns=[
    path('', Home.as_view(),name='home'),
    path('add-student/', Add_Student.as_view(),name='add-student'),
    path('delete_student/',Delete_student.as_view(), name='delete_student'),
    path('edit_student/<int:id>/',Edit_student.as_view(), name='edit_student'),
]