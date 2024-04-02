from django.urls import path
from . import views


urlpatterns=[
    path('join/',views.create_student,name='joiningform'),
    path('login/',views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout'),

]