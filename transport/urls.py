from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('transportfarmer/', views.transportfarmer, name="transportfarmer"),
    path('transportfarm/', views.transportfarm, name="transportfarm"),
    path('payment/', views.payment, name="payment"),
    path('login_view/', views.login_view, name="login_view"),
    path('signup/', views.signup, name="signup"),
    path('log_out/', views.log_out, name="log_out"),
    path('transdetails/', views.transdetails, name="transdetails"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)