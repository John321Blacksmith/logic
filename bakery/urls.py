from django.urls import path
from . import views

app_name = 'bakery'
urlpatterns = [
	path('', views.BreadList.as_view()),
	path('<int:pk>/', views.BreadDetail.as_view()),
]