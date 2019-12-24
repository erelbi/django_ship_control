from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Ship, Cargo, Remark, Information, Master
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Infoform, Engineerdata
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.template import loader

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.views import View
from django.contrib.auth.decorators import permission_required
class IndexView(View):
    
  
    def __init__(self):
        self.ships = Ship.objects.all().order_by("-id")
        self.cargo = Cargo.objects.all().order_by("-id")
        self.remark = Remark.objects.all().order_by("-id")

    def view_flag(self):
        flag = (self.ships)
        return flag
      

    def view_ship(self):
        ship_name = self.ships
        return ship_name

    def view_cargo(self):
        cargo = self.cargo
        return cargo

    def get(self,request, *args, **kwargs):
        s1 = IndexView()
        flag = s1.view_flag()
        ships = s1.view_ship()
        cargo = s1.view_cargo()
        response = TemplateResponse(request, 'home.html', {'ships':ships, 'cargo':cargo,})
        eng = Engineer("Turkey",3000)
        print(eng.get_info())
        return response
# def home(request):
#     try:
#         ships = Ship.objects.all().order_by("-id")
#         cargo = Cargo.objects.all().order_by("-id")
        
#         remark = Remark.objects.all().order_by("-id")
#     except:
#         ships()
#         cargo()
#         remark()
 
#     return render(request, 'home.html' , {'ships':ships, 'cargo':cargo, 'remark':remark})


class Personel(object):
    def __init__(self,national):
        self.national = national
        self.personel_info = dict()

    def get_info(self):
        self.personel_info['national'] = self.national
        return self.personel_info


class Engineer(Personel):
    def __init__(self,national,limit):
        self.limit = limit
        Personel.__init__(self,national)

    def get_info(self):
        self.personel_info['national'] = self.national
        self.personel_info['limit'] = self.limit
        return self.personel_info

def add_engineer(request):
    if request.method == 'POST':
       
        form = Engineerdata(request.POST)
   
        if form.is_valid():
            post = form.save(commit=False)
    
            post.save()
            messages.success(request, "You successfully updated the post")

            context= {'form': form}

            return render(request, 'addengine.html', context)
    
    else:
        form = Engineerdata()
        
    return render(request, 'addengine.html',{'form': form})



    
        

def ship_lastports(request,pk):
    try:
        ships = Ship.objects.get(pk=pk) 
        information = Information.objects.get(pk=pk)
        remark = Cargo.objects.get(pk=pk)
        if  Remark.objects.get(pk=pk) != None :
            psc = Remark.objects.get(pk=pk)
        else:
            pass
        #burada düşünülecek
            

           
    except Ship.DoesNotExist:
        raise Http404
    return render(request, 'lastport.html', {'ships':ships, 'information':information, 'remark':remark, 'psc':psc  })


@csrf_protect
def shipinformation(request):
    if request.method == "GET":
        try:
            master = Master.objects.all().order_by("id")
            ship = Ship.objects.all().order_by("-id")
            group = Group.objects.get(name='master')
            usersList = User.objects.all().order_by("-id")
        except:
            master()
            ship()
            usersList()
        return render(request, 'shipinfo.html', {'master':master, 'ship':ship, 'usersList':usersList})
    
    if request.method == 'POST':
        try:
            Information.objects.create(
                captain = request.POST.get("captain"),
                ship = request.POST.get("ship"),
                imo = request.POST.get("imo"),
                mmsi = request.POST.get("mmsi"),
                callsign = request.POST.get("callsign"),
                gross = request.POST.get("gross"),
                deadweight = request.POST.get("deadweight"),
                buildyear = request.POST.get("buildyear"))
            return  JsonResponse({"code":200,"data":None,"msg":"Added successfully"})
        except Exception as e:
            return  JsonResponse({"code":500,"data":str(e),"msg":"add failed"})  
   
@login_required 
def info_get(request):
    if request.method == 'POST':
       
        form = Infoform(request.POST)
   
        if form.is_valid():
            post = form.save(commit=False)
    
            post.save()
            messages.success(request, "You successfully updated the post")

            context= {'form': form}

            return render(request, 'postinfo.html', context)
    
    else:
        form = Infoform()
        
    return render(request, 'postinfo.html',{'form': form})

@permission_required('auth.view_user')
@login_required 
@csrf_protect
def info_edit(request,pk):

    # IndexView.__init__():
    master = Master.objects.get(pk=pk) 
    info = get_object_or_404(Information, pk=pk)
    if request.method == "POST":
        form = Infoform(request.POST, instance=info)
        if form.is_valid():
            post = form.save(commit=False)
            if master.master == request.user:
                post.author = request.user
                post.save()
            else:
                response = TemplateResponse(request, 'permission.html')
                return response
            messages.success(request, "You successfully edit Information of the ship")
            return redirect('ship_lastport', pk=post.pk)
    else:
        form = Infoform(instance=info)
    return render(request, 'infoedit.html', {'form': form})
    


def signup(request, pk):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



    # def cargo(request, pk):
    
#     ship = get_object_or_404(Ship, pk=pk)
#     if request.method == 'POST':
#         cargo = request.POST['cargo']
#         message = request.POST['information']

#         user = User.objects.first()  

#         cargo = Cargo.objects.create(
#             cargo=cargo,
#             ship=ship,
#             starter=user
#         )

#         remark = Remark.objects.create(
#             message=message,
#             cargo=cargo,
#             created_by=user
#         )

#         return redirect('ship_lastport', pk=ship.pk)  

#     return render(request, 'newport.html', {'ship': ship})