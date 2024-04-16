from django.shortcuts import render
from django.http import HttpResponse
from .models import farmerdetail,landdetail,log_sign
from django.contrib.auth.models import User
import random
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


praveen={}
# Create your views here.
def index(request):
    log_name= request.user
    return render(request, 'contract/index.html',{'username':log_name})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            log_name = request.user
            login(request,user)
            return render(request, 'agriforlife/index_one.html', {'username': log_name})
        else:
            return redirect('/pagerror')
    else:
        return render(request, 'contract/login_view.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            logsign = log_sign(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            logsign.save()
            user.save()
            return redirect('/contract/details')
        except:
            return redirect('/pagerror')
    else:
        return render(request, 'contract/signup.html')



def contracts(request):
    prajwal=None;
    if request.method == 'POST':
        randometext = request.POST['inputRandomText']
        contractid = request.POST['contractid']
        try:
            landobject= landdetail.objects.get(land_id=contractid)
            print(landobject)
        except:
            return redirect('/pagerror')
        if (randometext == landobject.generated_id):
            prajwal= True
            mahadev = {'contract_id':contractid, 'Survey_Number':landobject.land_survey, 'dimension':landobject.land_dimension, 'area':landobject.land_area, 'irrigation':landobject.land_typeirrigation, 'prajwal':prajwal }
            return render(request, 'contract/contracts.html', mahadev)
        else:
            prajwal=None
            return redirect('/pagerror')
    else:
        return render(request, 'contract/contracts.html')



def log_out(request):
    logout(request)
    return render(request, 'contract/log_out.html')



def details(request):

    if request.method =='POST':
    
        name = request.POST.get('inputname', '')
        farmerusername = request.POST.get('inputusername', '')
        mailid = request.POST.get('inputEmail', '')
        address1 = request.POST.get('inputAddress', '')
        address2 = request.POST.get('inputAddress2', '')
        city = request.POST.get('inputCity', '')
        state = request.POST.get('inputState', '')
        zipcode = request.POST.get('inputZip', '')
        phone = request.POST.get('inputPhone', '')

        # Farmerdetail = farmerdetail(farmer_name=name, farmer_email=mailid, farmer_address1=address1+address2, farmer_city=city, farmer_state= state, farmer_zip=zipcode, farmer_phone=phone)
        # Farmerdetail.save()
        pini = (len(name)>0 and len(mailid)>0 and len(address1)>0 and len(address2)>0 and len(city)>0 and len(state)>0 and len(zipcode)>0 and len(phone)>0)
        print(pini)
        try:
            if (pini == True):
                log_name = request.user
                Farmerdetail = farmerdetail(farmer_name=name, farmer_address1=address1+address2,  farmer_email=mailid, farmer_city=city, farmer_state= state, farmer_zip=zipcode, farmer_phone=phone, username=request.user)
                Farmerdetail.save()
                print(Farmerdetail.username)
                return render(request, 'contract/login_view.html')

            else:
                return render(request, '/pagerror.html')
        except:
            return redirect('/pagerror')

    return render(request, 'contract/details.html')



def FarmDetails(request):

    if request.method =='POST':
        naam = request.POST.get('usernames','')
        dimension = request.POST.get('dimension', '')
        pH = request.POST.get('inputSoilpH', '')
        area = request.POST.get('inputFarmArea', '')
        s_no = request.POST.get('SurveyNumber', '')
        crop = request.POST.get('croptype', '')
        nitrogen = request.POST.get('inputSoilNitrogen', '')
        phosphorous = request.POST.get('inputSoilPhosphorous', '')
        pottassium = request.POST.get('inputSoilPottassium', '')
        sulphur = request.POST.get('inputSoilSulphur', '')
        calcium = request.POST.get('inputSoilCalcium', '')
        magnesium = request.POST.get('inputSoilMagnesium', '')
        irrigate = request.POST.get('irrigation', '')
    
        pini_1 = (len(naam)>3 and len(dimension)>3 and len(pH)>0 and len(area)>0 and len(s_no)>3 and len(crop)>3 and len(nitrogen)>0 and len(phosphorous)>0 and len(pottassium)>0 and len(sulphur)>0 and len(calcium)>0 and len(magnesium)>0 and len(irrigate)>3) 
        print(pini_1)

        try:
            if (pini_1 == True):
                print(pini_1)
                def generate_random_text(length):
                    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                    text = ''.join(random.sample(characters, length))
                    return text
                    
                
                generated_id=generate_random_text(10)
                
                
                log_name=request.user
                print(log_name)
                LandDetail = landdetail(land_name=naam, generated_id=generated_id, land_dimension=dimension, land_ph=pH, land_area=area, land_survey=s_no, land_crop=crop, land_nitrogen=nitrogen, land_phosphorous=phosphorous, land_pottassium=pottassium, land_sulphur=sulphur, land_calcium=calcium, land_magnesium=magnesium, land_typeirrigation=irrigate, username=request.user)
                LandDetail.save()

                id_1 = LandDetail.land_id
                praveen['land_id']=id_1
                praveen['gen_id']=generated_id
                # praveen = {'land_id':id_1 ,'gen_id':generated_id}
                return render(request, 'contract/contractdetails.html', praveen)
            else:
                return render(request, '/pagerror.html')
        except:
            return redirect('/pagerror')
       
    return render(request, 'contract/FarmDetails.html')





def contractdetails(request):
    return render(request, 'contract/contractdetails.html')



def tracker_1(request):
    return render(request, 'contract/tracker_1.html')




