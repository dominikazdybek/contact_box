from django.shortcuts import render
from django.views import View
from contact_list.models import Contact,Adress
from django.http.response import HttpResponseRedirect

class ContactAddAddressView(View):
	def get(self,request,my_id):
		contact = Contact.objects.get(id=my_id)
		addresses = Adress.objects.filter(contact=contact)
		context = {"contact" : contact,
			"addresses" : addresses,
			"author":"Dominika",
			"year":2017}
		print("GET LandingView")
		return render(request, "contact/contact_add_address.html",context)

	def post(self, request, my_id):
		#validate input from form
		contact = Contact.objects.get(id=my_id)
		address = Adress()
		address.city = request.POST.get("city")
		address.street= request.POST.get("street")
		address.number_of_house= request.POST.get("number")
		address.contact = contact
		address.save()
		return HttpResponseRedirect("/contact/modify/" + my_id)
