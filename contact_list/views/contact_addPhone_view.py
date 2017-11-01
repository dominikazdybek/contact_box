from django.shortcuts import render
from django.views import View
from contact_list.models import Contact,Phone
from django.http.response import HttpResponseRedirect

class ContactAddPhoneView(View):
	def get(self,request,my_id):
		contact = Contact.objects.get(id=my_id)
		phones = Phone.objects.filter(contact=contact)
		context = {"contact":contact,
			"phones":phones,
			"author":"Dominika",
			"year":2017}
		print("GET LandingView")
		return render(request, "contact/contact_add_phone.html",context)

	def post(self, request, my_id):
		#validate input from form
		contact = Contact.objects.get(id=my_id)
		phone = Phone()
		phone.number = request.POST.get("number")
		phone.type_of_phone = request.POST.get("phone type")
		phone.contact = contact
		phone.save()
		return HttpResponseRedirect("/contact/modify/" + my_id)
