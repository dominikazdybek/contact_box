"""warsztat_3_contact_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from contact_list.views.landing_view import LandingView
from contact_list.views.contact_list_view import ContactListView
from contact_list.views.contact_add_view import ContactAddView
from contact_list.views.contact_modify_view import ContactModifyView
from contact_list.views.contact_delete_view import ContactDeleteView
from contact_list.views.contact_show_view import ContactShowView
from contact_list.views.contact_addAddress_view import ContactAddAddressView
from contact_list.views.contact_addPhone_view import ContactAddPhoneView
from contact_list.views.contact_addEmail_view import ContactAddEmailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^/?$', LandingView.as_view()),
    url(r'^contact/list$', ContactListView.as_view()),
    url(r'^contact/add$', ContactAddView.as_view()),
    url(r'^contact/modify/(?P<my_id>(\d)+)$', ContactModifyView.as_view()),
    url(r'^contact/delete/(?P<my_id>(\d)+)$', ContactDeleteView.as_view()),
    url(r'^contact/show/(?P<my_id>(\d)+)$', ContactShowView.as_view()),
    url(r'^contact/(?P<my_id>(\d)+)/addAddress$', ContactAddAddressView.as_view()),
    url(r'^contact/(?P<my_id>(\d)+)/addPhone$', ContactAddPhoneView.as_view()),
    url(r'^contact/(?P<my_id>(\d)+)/addEmail$', ContactAddEmailView.as_view()),


]
