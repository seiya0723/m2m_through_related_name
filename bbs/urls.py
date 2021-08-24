from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [ 
    path('', views.index, name="index"),
    path('good/<int:pk>/', views.good, name="good"),
    path('bad/<int:pk>/', views.bad, name="bad"),
]

