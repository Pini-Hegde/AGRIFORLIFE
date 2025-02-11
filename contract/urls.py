"""agriforlife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login_view/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('log_out/', views.log_out, name='log_out'),
    path("details/", views.details, name="details"),
    path("FarmDetails/", views.FarmDetails, name="FarmDetails"),
    path("contractdetails/", views.contractdetails, name="contractdetails"),
    path("contracts/", views.contracts, name="contracts"),
    path("tracker_1/", views.tracker_1, name="tracker_1"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
