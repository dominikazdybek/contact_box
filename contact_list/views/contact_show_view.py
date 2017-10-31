from django.shortcuts import render
from django.views import View
from contact_list.models import Contact
from django.http.response import HttpResponseRedirect

class ContactShowView(View):
	def get(self,request,my_id):
		contact = Contact.objects.get(id=my_id)
		context = {"contact" : contact,
			"author":"Dominika",
			"year":2017}
		print("GET LandingView")
		return render(request, "contact/contact_show.html",context)
	
	def post(self, request, my_id):
		#validate input from form 
		modify_from_form = request.POST.get('modify')
		cancel_from_form = request.POST.get('cancel')
		print(modify_from_form,cancel_from_form)
		if modify_from_form:
			return HttpResponseRedirect("/contact/modify/" + my_id)
		else:
			return HttpResponseRedirect("/contact/list")
	

