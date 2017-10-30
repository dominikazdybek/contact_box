from django.shortcuts import render
from contact_list.models import Contact

# Create your views here.

def landing_page(request):
	return render(request, "landing.html")

