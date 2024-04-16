from django.db import models
from django.contrib.auth.models import User

class log_sign(models.Model):
    username = models.CharField(primary_key=True, unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class farmerdetail(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=100, default="")
    farmer_address1 = models.CharField(max_length=100, default="")
    farmer_email = models.CharField(max_length=100, unique=True, default="")
    farmer_city = models.CharField(max_length=100, default="")
    farmer_state = models.CharField(max_length=100, default="")
    farmer_zip = models.CharField(max_length=100, default="")
    farmer_phone = models.CharField(max_length=100, default="")
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.farmer_name



class landdetail(models.Model):
    land_id = models.AutoField(primary_key=True)
    land_name = models.CharField(max_length=20, default='')
    generated_id= models.CharField(max_length=60, default='')
    land_dimension = models.CharField(max_length=100, default='')
    land_ph = models.CharField(max_length=100, default='')
    land_area = models.CharField(max_length=100, default='')
    land_survey = models.CharField(max_length=100,unique=True, default='')
    land_crop = models.CharField(max_length=100, default='')
    land_nitrogen = models.CharField(max_length=100, default='')
    land_phosphorous = models.CharField(max_length=100, default='')
    land_pottassium = models.CharField(max_length=100, default='')
    land_sulphur = models.CharField(max_length=100, default='')
    land_calcium = models.CharField(max_length=100, default='')
    land_magnesium = models.CharField(max_length=100, default='')
    land_typeLand = models.CharField(max_length=100, default='')        
    land_typeirrigation = models.CharField(max_length=100, default='')
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.land_name





class transporttruck(models.Model):
    transport_id=models.AutoField(primary_key=True)
    t_name=models.CharField(max_length=50, default='')
    t_genereted_id = models.CharField(max_length=10, default='')
    t_Email=models.CharField(max_length=50, default='')
    t_phone=models.CharField(max_length=50, default='')
    t_from=models.CharField(max_length=50, default='')
    t_where=models.CharField(max_length=50, default='')
    t_date=models.DateField( default='')
    t_weight=models.CharField(max_length=50, default='')
    t_message=models.CharField(max_length=50, default='')
    t_price=models.CharField(max_length=50, default='')
    t_payment=models.CharField(max_length=50, default='')
    username=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.t_name

class contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=50, default='')
    # cemail=models.ForeignKey(log_sign, on_delete=models.CASCADE)
    cemail = models.CharField(max_length=50, default='')
    cnumber=models.CharField(max_length=50, default='')
    ccrop=models.CharField(max_length=50, default='')
    caddress=models.CharField(max_length=50, default='')

    def __str__(self):
        return self.cname



