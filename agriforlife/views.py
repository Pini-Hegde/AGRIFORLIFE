from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from contract.models import contact


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        crop = request.POST['cropname']
        addr = request.POST['address']

        print(name)
        print(email)
        print(number)
        print(crop)
        print(addr)


        var = (len(name)>0 and len(email)>0 and len(number)>0 and len(crop)>0 and len(addr)>0)
        print(var)

        try:
            if(var == True):
                Contact = contact(cname=name, cemail=email, cnumber=number, ccrop=crop, caddress=addr)
                Contact.save()
                return render(request, 'agriforlife/index.html')
        except:
            return redirect('/pagerror')
    
    return render(request, 'agriforlife/index.html')



def pagerror(request):
    return render(request, 'agriforlife/pagerror.html')


def index_one(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        crop = request.POST['cropname']
        addr = request.POST['address']

        print(name)
        print(email)
        print(number)
        print(crop)
        print(addr)


        var = (len(name)>3 and len(email)>3 and len(number)>3 and len(crop)>3 and len(addr)>3)
        print(var)

        

        try:
            if(var == True):
                Contact = contact(cname=name, cemail=email, cnumber=number, ccrop=crop, caddress=addr)
                Contact.save()
                return render(request, 'agriforlife/index_one.html')
        except:
            return redirect('/pagerror')
    
    return render(request, 'agriforlife/index_one.html')










