from django.shortcuts import render
from django.views import View
from contact_list.models import Contact

class ContactListView(View):
	def get(self,request):
		contacts = Contact.objects.all()
		context = {"contacts" : contacts,
			"author":"Dominika",
			"year":2017}
		print("GET LandingView")
		return render(request, "contact/contact_list.html",context)
	
