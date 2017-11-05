from django.shortcuts import render
from django.views import View
from contact_list.models import Group
from django.http.response import HttpResponseRedirect


class GroupsDeleteView(View):
	def get(self,request,my_id):
		context = {"author":"Dominika",
			"year":2017}
		return render(request, "contact/groups_delete.html",context)

	def post(self,request,my_id):
		#validate input from form
		yes_form = request.POST.get("delete_group")
		cancel_form = request.POST.get("cancel")
		if yes_form:
			group = Group.objects.get(id=my_id)
			group.delete()
			return HttpResponseRedirect("/groups/list")
		else:
			pass

		return HttpResponseRedirect("/groups/list")
