from django.urls import path
from . import views

app_name = 'market'
# url patterns of the app here 

urlpatterns = [
	# index page pattern
	path('', views.index, name='index'),
]