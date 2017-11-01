from django.shortcuts import render
from django.views import View
from contact_list.models import Contact,Email
from django.http.response import HttpResponseRedirect

class ContactAddEmailView(View):
	def get(self,request,my_id):
		contact = Contact.objects.get(id=my_id)
		emails = Email.objects.filter(contact=contact)
		context = {"contact" : contact,
			"emails": emails,
			"author":"Dominika",
			"year":2017}
		print("GET LandingView")
		return render(request, "contact/contact_add_email.html",context)

	def post(self, request, my_id):
		#validate input from form
		contact = Contact.objects.get(id=my_id)
		email = Email()
		email.email = request.POST.get("email")
		email.type_of_email = request.POST.get("email type")
		email.contact = contact
		email.save()
		return HttpResponseRedirect("/contact/modify/" + my_id)
