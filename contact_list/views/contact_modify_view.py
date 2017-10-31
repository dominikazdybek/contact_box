from django.shortcuts import render
from django.views import View
from contact_list.models import Contact
from django.http.response import HttpResponseRedirect


class ContactModifyView(View):
	def get(self,request,my_id):
		context = {"author":"Dominika",
			"year":2017}
		return render(request, "contact/contact_modify.html",context)

	def post(self,request,my_id):
		#validate input from form 
		contact = Contact.objects.get(id=my_id)
		contact.name = request.POST.get("name")
		contact.surname = request.POST.get("surname")
		contact.description = request.POST.get("description")
		contact.save()
		return HttpResponseRedirect("/contact/list")
	
