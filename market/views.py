import psycopg2
from django.shortcuts import render
# Create your views here.



def index(request):
	"""This function renders a main page of the market."""

	return render(request, 'market/index.html')