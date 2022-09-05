
from django import views
from django.shortcuts import render
from Admin_dashboard.models import*

def home(request):
    slider = SlidersImagesModel.objects.all()
    print(slider)
    return render(request, 'web/home.html',{'sliders':slider})