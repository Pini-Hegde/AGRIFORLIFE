import random
from django.shortcuts import render,redirect
from contract.models import transporttruck, log_sign
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from .models import 

# Create your views here.
d={}

def login_view(request):
    if request.method == 'POST':
        username = request.POST['tusername']
        password = request.POST['tpassword']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            log_name = request.user
            login(request,user)
            return render(request, 'transport/transportfarmer.html', {'username':log_name})
        else:
            return redirect('/pagerror')
    else:
        return render(request, 'transport/login_view.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['tusername']
        password = request.POST['tpassword']
        email = request.POST['temail']
        first_name = request.POST['tfirst_name']
        last_name = request.POST['tlast_name']
        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            logsign = log_sign(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            logsign.save()
            user.save()
            return redirect('/transport/login_view')
        except:
            return redirect('/pagerror')
    else:
        return render(request, 'transport/signup.html')


def log_out(request):
    logout(request)
    return render(request, 'transport/log_out.html')


def transportfarmer(request):
    user=User
    log_name=request.user
    return render(request, 'transport/transportfarmer.html', {'username':log_name})


def transportfarm(request):
    if request.method=='POST':
        name=request.POST.get('Name','')
        username=request.POST.get('username','')
        emailid=request.POST.get('email','')
        phone=request.POST.get('phone','')
        fromplace=request.POST.get('fromplace','')
        destplace=request.POST.get('destplace','')
        date=request.POST.get('date','')
        weight=request.POST.get('weight','')
        distance=request.POST.get('distance','')
        msg=request.POST.get('msg','')

        var_1= (len(name)>3 and len(username)>3 and len(emailid)>3 and len(phone)>0 and len(fromplace)>3 and len(destplace)>3 and len(date)>0 and len(weight)>0)
        print(var_1)

        if var_1 == True:
            d['dname']=name
            d['dusername']=username
            d['demailid']=emailid
            d['dphoneno']=phone
            d['dfromplace']=fromplace
            d['ddestplace']=destplace
            d['ddate']=date
            d['dweight']=weight
            d['ddistance']=distance
            d['dmsg']=msg


            price=99.9
            kdw = float((float(d['dweight']))/20.0)
            amount = (price * float(d['ddistance'])) * kdw
            print(amount)
            d['damount']=int(amount)

            return render(request, 'transport/payment.html', d)
        else:
            redirect('/pagerror')

    return render(request, 'transport/transportfarm.html')


def payment(request):
    
    if request.method == 'POST':

        pay=request.POST.get('payment','')

        if len(pay) > 3:

            d['dpayment']=pay


            def generate_random_text(length):
                characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                text = ''.join(random.sample(characters, length))
                return text
            generated_id=generate_random_text(10)
            d['gen_id']=generated_id


            transtruck = transporttruck(t_name= d['dname'], t_genereted_id=d['gen_id'], t_Email=d['demailid'], t_phone=d['dphoneno'], t_from=d['dfromplace'], t_where=d['ddestplace'], t_date=d['ddate'], t_weight=d['dweight'], t_message=d['dmsg'], t_price= d['damount'], t_payment=d['dpayment'],  username=request.user)
            transtruck.save()

            t_id = transtruck.transport_id
            d['t_id']=t_id
            

            return render(request, 'transport/transdetails.html', d)

        else:
            return render(request, 'pagerror.html')

    return render(request, 'transport/payment.html')


def transdetails(request):
    return render(request, 'transport/transdetails.html')
        
