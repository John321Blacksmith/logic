from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
	# collection & object API endpoints for milk
	path('milk/', views.MilkList.as_view()),
	path('milk/<int:pk>/', views.MilkDetail.as_view()),

	# collection & object API endpoints for kefir
	path('kefir/', views.KefirList.as_view()),
	path('kefir/<int:pk>/', views.KefirDetail.as_view()),

	# collection & object API endpoints for cheese
	path('cheese/', views.CheeseList.as_view()),
	path('cheese/<int:pk>/', views.CheeseDetail.as_view()),

	# collection & object API endpoints for cabbage-cheese
	path('cabbage-cheese/', views.CabbCheeseList.as_view()),
	path('cabbage-cheese/<int:pk>/', views.CabbCheeseDetail.as_view()),
]