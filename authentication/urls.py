from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from authentication import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Knowledge Platform Admin"
admin.site.site_title = "Knowledge Platform Admin Portal"
admin.site.index_title = "Welcome to CData Knowledge Platform"

urlpatterns = [
   path('', views.index, name="home"),
   path('signup', views.signup, name="signup"),
   path("contribute", views.contribute, name='contribute'),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('activate/<uidb64>/<token>/', views.activate, name="activate"),
   path('defects', views.defects,name='defects'),
   path('defect', views.defect,name='defect'),
   path('enhancements', views.enhancements,name='enhancements'),
   path('supportticket', views.supportticket,name='supportticket'),
   path('opportunity', views.opportunity,name='opportunity'),
   path('jira', views.jira,name='jira'),
   path('jiradisplay', views.jiradisplay,name='jiradisplay'),
   path('freshdesk', views.freshdesk,name='freshdesk'),
   path('freshdeskdisplay', views.freshdeskdisplay,name='freshdeskdisplay'),
   path('salesforce', views.salesforce,name='salesforce'),
   path('salesforcedisplay', views.salesforcedisplay,name='salesforcedisplay'),
   path('search', views.search, name="search"),
   path('your_contribution', views.your_Contribution, name="contri"),
   path('update_contribution', views.update_contribution, name="update_contribution"),
   path('update_contribution_display', views.update_contribution_display, name="update_contribution_display"),
   path('update_data', views.update_data, name="update_data"),
   path('zoho', views.Zoho, name = "zoho"),
   
]