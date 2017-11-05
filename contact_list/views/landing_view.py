from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

class LandingView(View): # klasa dziedziczy po klasie View
	def get(self,request):	#implementuja takie metody jak requesty
		context = {"author":"Dominika",
			"year":2016}
		print("GET LandingView")
		return render(request, "landing.html",context) # tu normalnie piszemy widok


	def post(self,request):
		return Httpresponse("Przyszedł request POST")
