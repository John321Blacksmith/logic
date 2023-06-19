from django.urls import path
from . import views


app_name = 'grocery'
urlpatterns = [
	path('vegetables/', views.VegetableList.as_view()),
	path('vegetables/<int:pk>/', views.VegetableDetail.as_view()),
	
	path('fruits/', views.FruitList.as_view()),
	path('fruits/<int:pk>/', views.FruitDetail.as_view()),

]
