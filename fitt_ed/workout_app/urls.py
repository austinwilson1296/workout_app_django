from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='home'),
    path('about/',views.about,name='about'),
    path('pricing/',views.price,name='price'),
    path('workout_creator/',views.workout,name='workout'),
    path('experience-level/<str:level>/', views.experience_level, name='experience_level'),
    
]