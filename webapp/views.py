

from django import views
from django.shortcuts import render
from django.views import View

from Admin_dashboard.models import*

class HomePageView(View):
    def get(self, request):
        slider = SlidersImagesModel.objects.all().order_by("-id")
        brand = BrandsModel.objects.all()
        return render(request, 'web/home.html',{'sliders':slider, 'brand':brand})


class BrandTeamplatesView(View):
    def get(self, request):
        brand = BrandsModel.objects.all()
        return render(request, 'web/brand.html',{'brand':brand})


class SAirBrandsView(View):
    def get(self, request):
     
        return render(request, 'web/S-air.html')        
          

class CataloueView(View):
    def get(self, request):
        data = CatalagueModel.objects.all()
        return render(request, 'web/catalogue.html', {'catalogue':data})        
                              

