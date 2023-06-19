from django.urls import path
from . import views

app_name = 'butchers'
urlpatterns = [
	path('', views.MeatList.as_view()),
	path('<int:pk>/', views.MeatDetail.as_view()),
]