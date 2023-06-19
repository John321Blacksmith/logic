from django.urls import path
from . import views

app_name = 'butchers'
urlpatterns = [
	path('butchers/', views.MeatList.as_view()),
	path('butchers/<int:pk>/', views.MeatDetail.as_view()),
]