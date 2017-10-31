from django.shortcuts import render
from django.views import View
from contact_list.models import Contact
from django.http.response import HttpResponseRedirect


class ContactDeleteView(View):
	def get(self,request,my_id):
		context = {"author":"Dominika",
			"year":2017}
		return render(request, "contact/contact_delete.html",context)

	def post(self,request,my_id):
		#validate input from form 
		yes_from_form = request.POST.get('yes')
		cancel_from_form = request.POST.get('cancel')
		if yes_from_form:
			contact = Contact.objects.get(id=my_id)
			contact.delete()
		else:
			pass

		return HttpResponseRedirect("/contact/list")
	
