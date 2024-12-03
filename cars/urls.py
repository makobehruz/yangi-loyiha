from django.urls import path
from . import views

app_name = 'cars'

urlpatterns =[

    path('', views.post_list, name ='post_list'),
    path('post/create/', views.post_create, name = 'post_create')
]