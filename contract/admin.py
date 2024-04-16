from django.contrib import admin
from .models import  farmerdetail,landdetail,log_sign,transporttruck,contact

# Register your models here.

admin.site.register(landdetail)
admin.site.register(farmerdetail)
# admin.site.register(log_sign)
admin.site.register(transporttruck)
admin.site.register(contact)
