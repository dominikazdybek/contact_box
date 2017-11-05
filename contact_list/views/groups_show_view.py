from django.shortcuts import render
from django.views import View
from contact_list.models import Contact,Group
from django.http.response import HttpResponseRedirect

class GroupsShowView(View):
	def get(self,request,my_id):
		group = Group.objects.get(id=my_id)
		contacts= group.contact_set.all()
		context = {"contacts" : contacts,
			"group" :group,
			"author":"Dominika",
			"year":2017}
		print("GET LandingView")
		return render(request, "contact/groups_show.html",context)

	def post(self, request, my_id):
		#validate input from form
		delete_from_form = request.POST.get("contact_id")
		cancel_from_form = request.POST.get("cancel")
		if delete_from_form:
			group = Group.objects.get(id=my_id)
			cont = Contact.objects.get(name=delete_from_form)
			cont.groups.remove(group)
			cont.save()
			return self.get(request,my_id)
		else:
			return HttpResponseRedirect("/groups/list")
