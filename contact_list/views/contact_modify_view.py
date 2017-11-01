from django.shortcuts import render
from django.views import View
from contact_list.models import Contact, Adress, Phone, Email
from django.http.response import HttpResponseRedirect


class ContactModifyView(View):
	def get(self,request,my_id):
		contact = Contact.objects.get(id=my_id)
		addresses = Adress.objects.filter(contact=contact)
		phones = Phone.objects.filter(contact=contact)
		emails = Email.objects.filter(contact=contact)
		context = {"contact":contact,
		"addresses" : addresses,
		"phones" :phones,
		"emails":emails,
		"author":"Dominika",
			"year":2017}
		return render(request, "contact/contact_modify.html",context)

	def post(self,request,my_id):
		contact = Contact.objects.get(id=my_id)
		#validate input from form
		if request.POST.get('modify'):
			contact.name = request.POST.get("name")
			contact.surname = request.POST.get("surname")
			contact.description = request.POST.get("description")
			contact.save()
			return HttpResponseRedirect("/contact/list")
		elif request.POST.get('delete_address'):
			address_id= request.POST.get("address_id")
			address = Adress.objects.filter(contact=contact).filter(pk=address_id)
			address.delete()
			return self.get(request,my_id)
		elif request.POST.get('delete_phone'):
			phone_id= request.POST.get("phone_id")
			phone = Phone.objects.filter(contact=contact).filter(pk=phone_id)
			phone.delete()
			return self.get(request,my_id)
		elif request.POST.get('delete_email'):
			email_id= request.POST.get("email_id")
			email = Email.objects.filter(contact=contact).filter(pk=email_id)
			email.delete()
			return self.get(request,my_id)
