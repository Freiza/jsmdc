from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from auction.models import User,Lead,JAdmin,Sandghat
from .forms import LeadFileModelForm,LeadModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage    
from django.core.files.base import ContentFile
from django.conf import settings
# Create your views here.

def ghat(request):
    
    if not request.session.has_key('is_logged'):
        return redirect('/')

    if request.method =="POST":
        print(request.POST)

    sands = Sandghat.objects.all()
    print(sands)
    print("ppppppppppppppppppppppp")
    print(request.session.get('uname'))
    lead = Lead.objects.get(user_name=request.session.get('uname'))
    context={'sands':sands,'fname':request.session.get('fname'),'deposit':'500000'}#lead.deposit
    return render(request,"index.html",context)


def wallet(request):
    if not request.session.has_key('is_logged'):
        return redirect('/')
    uname = request.session.get('uname')
    l = Lead.objects.get(user_name=uname)
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    if request.method == "POST":
        
        m = request.POST.getlist('marrd[]')
        
        print(uname)
        
        print("ooooooooooooooooooooooooo")
        print(l)
        
        for i in m:
            
            k=Sandghat.objects.get(id=i)
            
            l.vghat.add(k)
            

        g = l.vghat.all()
       
        context = {'sands':g,'lead':l}
            
        return render(request,"wallet.html",context)

    context = {'sands':l.vghat.all(),"lead":l}

    return render(request,"wallet.html",context) 
     

def home_page(request):
    logout(request)
    if request.method =="POST":
        uname = request.POST['user_name']
        upass = request.POST['password']
        print(uname,upass)
        user = authenticate(username=uname,password=upass)
        print(user)
        if user is not None:
            login(request,user) 
            fname = user.first_name
            fid = user.id
            request.session['is_logged']=True
            request.session['fid']=fid
            request.session['fname']=fname
            request.session['uname']=uname
            print(user.first_name)
            print(fname)
            print(request.session.get('fname'))
            print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
            return ghat(request)
        else:
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            messages.error(request,'Bad Credentials')
            return redirect("")

    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")

def profile(request):
    return render(request,"profile.html")



@csrf_exempt
def lead_create(request):
    form = LeadModelForm()
    formlead = LeadFileModelForm()
   
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    if request.method =="POST":
        form = LeadModelForm(request.POST)
        formlead = LeadFileModelForm(request.FILES)
        for f in formlead:
            print(f)
        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        #print(form)
        #print(form.errors)
        #print(request.POST.lists())
        print(dict(request.FILES))

        #request.POST['authority_letter']
        print('yyyyyyyyyyyyyyyyyyyyyyyy')
      
        if form.is_valid():
            fleet_record= form.save(commit=False)
            fleet_record.jadmin = JAdmin.objects.get(user__email="ranjeet@gmail.com")
            form.save()
            uname = request.POST['user_name']
            uemail = request.POST['email_id']
            upassword = request.POST['password']
            myuser = User.objects.create_user(uname,uemail,upassword)#create_user
            ml = User.objects.get(username=uname)
            ml.is_active = False
            ml.save()
            print('sdfsdfssfsdfsdfs')
       
        print(formlead.errors)
        if formlead.is_valid():
            fs = FileSystemStorage()
            al = request.FILES['authority_letter']
            poap = request.FILES['photo_of_authorized_person']
            gd = request.FILES['gst_document']
            pp = request.FILES['pan_photo']
            ccf = request.FILES['client_credential_file']
            fs.save(al.name,al)
            print(al.name,al)
            fs.save(poap.name,poap)
            print(poap)
            fs.save(gd.name,gd)
            fs.save(pp.name,pp)
            fs.save(ccf.name,ccf)
            formlead = LeadFileModelForm(request.FILES)
            
            formlead.save()

            #fs.save(formlead.name,formlead)
            

            
        return redirect("/")
    context = {'form': form,'formlead':formlead, 'regopro':"Registration Page"}
    return render(request,"registration.html",context)

def lead_update(request):
    if not request.session.has_key('is_logged'):
        return redirect('/')
    uname = request.session.get('uname')
    lead = Lead.objects.get(user_name=uname)
    form = LeadModelForm(instance=lead)
    if request.method =="POST" and form is not None:
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form,'lead':lead,'regopro':"Profile Page"}
    return render(request,"profile.html",context)


def forgot_password(request):
    if request.method =="POST":
        uname = request.POST['username']
        upass = request.POST['password']
        o=User.objects.get(username=uname)
        print(o)
        o.set_password(upass)
        o.save()
        l="love"
        return render(request,"login.html")
    return render(request,"forgotpass.html")


def signout(request):
    logout(request)
    return render(request,'login.html')
    messages.success(request,"Logged Out Successfully!")