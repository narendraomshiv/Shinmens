from django.shortcuts import render
from django.views import View
import json
import requests

class HomePageView(View):
    def get(self, request):
        url = "https://shimen.microcms.io/api/v1/top"
        payload={}
        headers = {
        'X-MICROCMS-API-KEY': 'c84e302bd7ce42aeaa3de3f3a8ae5b1a98eb'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        text_data = response.text
        json_data = json.loads(text_data)
        brands = json_data['contents'][0]['brand'][::]
        tech_carousel = json_data['contents'][0]['tech_carousel'][::]
        carousel = json_data['contents'][0]['carousel'][::]
        return render(request, 'web/home.html', {'brands':brands, 'tech_carousel':tech_carousel, 'carousel':carousel})



class BrandTeamplatesView(View):
    def get(self, request):
        url = "https://shimen.microcms.io/api/v1/brand-product"
        payload={}
        headers = {
        'X-MICROCMS-API-KEY': 'c84e302bd7ce42aeaa3de3f3a8ae5b1a98eb'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        text_data = response.text
        json_data = json.loads(text_data)
        brands = json_data['contents'][::]
        return render(request, 'web/brand-index.html', {'brands':brands})


class SAirBrandsView(View):
    def get(self, request):
        
        return render(request,'web/S-air.html',)        

class SheatBrandsView(View):
    def get(self, request):
     
        return render(request,'web/s-heat-details.html')        
          

class SlashBrandsView(View):
    def get(self, request):
       
        return render(request,'web/slash-details.html')        
                              
class StxBrandsView(View):
    def get(self, request):
        return render(request,'web/stx-details.html')        
          
class CataloueView(View):
    def get(self, request):
        
        return render(request, 'web/catalogue.html')        
                              




class TechPageView(View):
    def get(self, request):
       
        return render(request,'web/tech-index.html')



class CorporateView(View):
    def get(self, request):
       
        return render (request,'web/corporate.html')



class NewsView(View):
    def get(self, request):
      
        return render(request,'web/news.html')
       
