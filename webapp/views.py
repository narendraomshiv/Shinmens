
from urllib.robotparser import RequestRate
from django import views
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator


from Admin_dashboard.models import*

class HomePageView(View):
    def get(self, request):
        slider = SlidersImagesModel.objects.all().order_by("-id")
        brand = BrandsModel.objects.all()
        data = TechPageModel.objects.all()
        return render(request,'web/home.html',{'sliders':slider,'brand':brand, 'tech':data})


class BrandTeamplatesView(View):
    def get(self, request):
        brand = BrandsModel.objects.all()
        return render(request, 'web/brand.html',{'brand':brand})


class SAirBrandsView(View):
    def get(self, request):
        air = SAirModel.objects.all()
        return render(request,'web/S-air.html',{'air':air})        
          

class CataloueView(View):
    def get(self, request):
        data = CatalogModel.objects.all()
        return render(request, 'web/catalogue.html',{'catalogue':data})        
                              




class TechPageView(View):
    def get(self, request):
        data = TechPageModel.objects.all()
        return render(request,'web/tech-index.html', {'data':data})



class CorporateView(View):
    def get(self, request):
        data = CorporateModel.objects.all()
        return render (request,'web/corporate.html',{'data':data})



class NewsView(View):
    def get(self, request):
        data = NewsModel.objects.all()
        return render(request,'web/news.html',{'data':data})
       
