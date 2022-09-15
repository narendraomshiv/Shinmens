from email.mime import image
import re

from unicodedata import name
from urllib.request import Request
from django import views
from django.shortcuts import render
from django.views import View
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse 
from django.shortcuts import redirect
# Create your views here.
class AdminHomePageView(View):    
    def get(self, request):    
        return render(request, 'dashboard/index.html')
    

login_required(login_url='admin-login')
def adminPanel(request):

    user1 = User.objects.filter(is_superuser=True)
    user = User.objects.all()
    # ===========user counter=======

    counter=0
    superuser=0
    staff=0
    active = 0
    for i in user:
        counter+=1
        if i.is_superuser == True:
            superuser+=1

        if i.is_staff == True:
            staff+=1
        
        if i.is_active == True:
            active+=1
   
    # =========== end =======
    d = { "user":user1,
          "counter_user":counter,
          "superuser":superuser,
          'staff':staff,
          "active":active,
     
        }
    if request.user.is_superuser == True:
        return render(request,'dashboard/index.html',d)
    else:
        return redirect('loginAdmin')

#=============LOGIN=============

class Login(View):
    def get(self, request):
        return render(request, 'dashboard/samples/login.html')
    def post (self, request, **kwargs):
     if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password') 
        print(email)
        print(password)
        user = authenticate(request, email = email, password = password)
        print(user)
        if user is not None:
            if User.objects.filter(email=email, is_superuser=True):
                login(request,user)
            return redirect("dashboardHome")
        else:
            messages.error(request, 'You Are Not Admin User')
     else:
        messages.error(request,'invalid user email id')
     return render(request,'dashboard/samples/login.html') 


####
def home(request):
    return render(request,'web/home.html')

    return render(request,'dashboard/samples/login.html')    


#=============LOGOUT=============    

def userlogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully..!!')
    return redirect('loginAdmin')

#=============END================#




#========== Add Users============#
def AddUser(request):
    if request.method == 'POST':
      
        username = request.POST.get('username')
        print(username)
        email = request.POST.get('email')
        print(email)
        phone_number = request.POST.get('phone_number')
        print(phone_number)
        password = request.POST.get('password')
        print(password)
        con_password = request.POST.get('password1')
        print(con_password)
        if password == con_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User Email  Already Exist.. ')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,phone_number=phone_number)
               
                user.save()
                messages.success(request, 'User Added Successfully..!!')
                return redirect('showUser')
            messages.error(request, 'Password Not Match ..!!')
    if request.user.is_superuser == True:
        return render(request,'dashboard/add_user.html')

    else:
        return HttpResponseRedirect('/') 

#====== Edit User Profile =========#
def  UpdateUserProfileView(request, id):
    if request.method == 'POST':
        
       
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
         
          
        super = request.POST.get('super')
        staff = request.POST.get('staff')
        active = request.POST.get('active')
        checklist = [False,False,False]
        
        if super=='True':
            checklist[0]=True
        if staff=='True':
            checklist[1]=True
        if active=='True':
            checklist[2]=True
        
        user = User.objects.get(id=id)
        if user is not None:
          
            user.username = username
            user.email = email
            user.phone_number = phone_number
           
            user.is_superuser=checklist[0]
            user.is_admin=checklist[1]
            user.is_active=checklist[2]
            user.save()
            messages.success(request, 'User Edit Successfully..!!') 
            return  redirect('showUser')
        
        else:
    
            messages.success(request, 'This User is not Found!!') 
            return  redirect('showUser')
        
                
        
        
    if request.user.is_superuser == True:      
        return render(request,'dashboard/edit_user.html',{"user":User.objects.get(id=id)})
    else:
        return HttpResponseRedirect('/')
    
def profile(request):
    if request.method == "GET" :
        ob = User.objects.get(id=request.user.id)   
        if request.user.is_superuser == True:
            return render(request,'dasboard/profile.html',{"all":ob})
        else:
            return HttpResponseRedirect('/')

#=============delete User=============
@login_required(login_url='login')
def deleteUser(request,id):
    a = User.objects.get(id=id)
    a.delete()
    messages.success(request, 'User Deleted Successfully..!!')
    return redirect('showUser')
# =========== end ==================  
#=========== Show User =======#
class ShowUserView(View):
    def get(self, request):
        user_data = User.objects.all().order_by("-id") 
        user_total = User.objects.all().count()
        paginator = Paginator(user_data,per_page=10) 
        page_number = request.GET.get('page')
        page_object= paginator.get_page(page_number)

        return render(request, 'dashboard/show_user_details.html',{'page_obj':page_object, 'user_total':user_total})


class SlidersImagesView(View):
    def get(self, request):
        return render(request, 'dashboard/add-sliders-images.html')
    def post(self, request):
        data = SlidersImagesModel()
        image  = request.FILES.get('image')
       
        data.image = image
        data.save()
        messages.success(request, 'Sliders Image Add  Successfully..!!')
        return redirect('showDetails')
        
class SlidersImagesDetailsView(View):
    def get(self, request):
        data = SlidersImagesModel.objects.all().order_by('-id')
        return render(request, 'dashboard/sliders-image-details.html', {'page_obj':data})        
        

class EditSliderImagesView(View):
    def get(self, request,id):
       data = SlidersImagesModel.objects.get(id=id)
       return render(request, 'dashboard/edit_slidebar-images.html', {'data':data})
    
    def post(self, request, id):
        image = request.FILES.get('image')
        date = request.POST.get('date')
  
        data = SlidersImagesModel(id=id, image=image, date=date).save()
        messages.success(request, 'Sliders Image Edit  Successfully..!!')
        return redirect('showDetails')
        
class DeleteSlidersImagesView(View):
    def get(self, request, id):
        data = SlidersImagesModel.objects.get(id=id)
        data.delete()
        messages.success(request, 'Sliders Image Delete  Successfully..!!')
        return redirect('showDetails')
        
        
        
#==== Brand ======#

class AddBrandView(View):
    def get(self, request):
        return render(request, 'dashboard/add-brands.html')       
    
    
    def post(self, request):
        data = BrandsModel()
        image = request.FILES.get('image')
        heading = request.POST.get('brand_headings')
        description = request.POST.get('description')
        other_description = request.POST.get('other_description')
        
        data.image = image
        data.headings = heading
        data.description = description
        data.other_description = other_description
        
        data.save()
        messages.success(request, 'Brand Added  Successfully..!!')
        return redirect('brandDetails')
        
        
class BrandsDetailsView(View):
    def get(self, request):
        data = BrandsModel.objects.all().order_by('-id')
        return render(request, 'dashboard/brand-details-page.html', {'page_obj':data})  


#====== contact Details ===
    def contactdetails(request):
        data = ContactModels.objects.all()
        return render(request, '' ,{'data':data})

#  ===== catalogue views  page ====
class AddCatalogueViews(View):
    def get(self, request):
        return render(request, 'dashboard/add-catalogue.html')
    def post(self, request):
        data = CatalogModel()
        image = request.FILES.get('image')
        Heading = request.POST.get('Heading')
        years = request.POST.get('years')
        data.image = image
        data.Heading = Heading
        data.years = years
        data.save()
        messages.success(request, 'Catalogue Added  Successfully..!!')
        return redirect('catalogueDetails')


class CatalagueListDetailsView(View):
    def get(self, request):
        data = CatalogModel.objects.all()
        return render(request,'dashboard/details-catalogue.html',{'data':data}) 


# Edit Catalague views .

class EditCatalogueView(View):
    def get(self, request, id):
        data = CatalogModel.objects.get(pk=id)
        print(data)
        return render(request,'dashboard/edit_catalog.html',{'data':data})
    def post(self,request, id):
        image = request.FILES.get('image')
        years = request.POST.get('years')
        Heading= request.POST.get('Heading')
        data = CatalogModel(id=id,
        image = image,
        years= years, 
        Heading = Heading).save()
        return redirect("catalogueDetails")


##### Delete Data ...
       
class DeleteCatalogView(View):
    def get(self, request, id):
        data = CatalogModel.objects.get(id=id)
        data.delete()
        messages.success(request, 'Catalog Data Deleted Successfully..!!')
        return redirect('catalogueDetails')
                
                
#===== Add Tech Views. ==== 
class AddTechView(View):
    def get(self, request):
        return render(request,'dashboard/add-tech.html')
        
    def post(self, request):
        data = TechPageModel()
        image = request.FILES.get('image')
        heading = request.POST.get('heading')
        title = request.POST.get('title')
        description = request.POST.get('description')
        data.image = image
        data.heading = heading
        data.title = title
        data.description = description
        data.save()
        messages.success(request,'Tech  Added  Successfully..!!')
        return redirect('techDetails')


class TechListDetailsView(View):
    def get(self, request):
        data = TechPageModel.objects.all()
        print(data)
        return render(request,'dashboard/all-tech-details.html',{'data':data}) 

#======  Edit Tech View pages. ===

class EditTechView(View):
    def get(self, request, id):
        data = TechPageModel.objects.get(pk=id)
        return render(request,'dashboard/edit-tech.html',{'data':data})
    def post(self,request, id):
        image = request.FILES.get('image')
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        data = TechPageModel(id=id,
        image = image,
        title = title,
        description = description, 
        heading = heading).save()
        return redirect("techDetails")


# === Delete Tech views .====
class DeleteTechView(View):
    def get(self, request, id):
        data = TechPageModel.objects.get(id=id)
        data.delete()
        messages.success(request,'Tech Data Deleted Successfully..!!')
        return redirect('techDetails')


# ======== news page views =====

class AddNewsViews(View):
    def get(self, request):
        return render(request, 'dashboard/add-news.html')
    def post(self, request):
        data = NewsModel()
        image = request.FILES.get('image')
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        date = request.POST.get('date')
        data.image = image
        data.heading = heading
        data.date = date
        data.title = title
        data.save()
        messages.success(request, 'News  Added  Successfully..!!')
        return redirect('newsDetails')



class NewsDetailsView(View):
    def get(self, request):
        data = NewsModel.objects.all()
        print(data)
        return render(request,'dashboard/all-new.html',{'data':data}) 



class EditNewsView(View):
    def get(self, request, id):
        data = NewsModel.objects.get(pk=id)
        return render(request,'dashboard/edit-new.html',{'data':data})
    def post(self,request, id):
        image = request.FILES.get('image')
        title = request.POST.get('title')
        heading = request.POST.get('heading')
        date = request.POST.get('date')
        data = NewsModel(id=id,
        image = image,
        title = title,
        date = date, 
        heading = heading).save()
        return redirect("newsDetails")


class DeleteNewsviews(View):
    def get(self, request, id):
        data = NewsModel.objects.get(id=id)
        data.delete()
        messages.success(request,'News Data Deleted Successfully..!!')
        return redirect('newsDetails')





