from django.shortcuts import render
from django.views import View
from contact_list.models import Group
from django.http.response import HttpResponseRedirect


class GroupsListView(View):
	def get(self,request):
		groups = Group.objects.all().order_by('name')
		context = {"groups" : groups,
			"author":"Dominika",
			"year":2017}
		#print("GET LandingView")
		return render(request, "contact/groups_list.html",context)

	def post(self,request):
		contact_name = request.POST.get("member")
		return redirect("groups/search/?name="+contact_name)
