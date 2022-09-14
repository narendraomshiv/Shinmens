from django.urls import path
from  .import views



urlpatterns = [
    path('', views.HomePageView.as_view(), name="homePage" ),
    path('brand/', views.BrandTeamplatesView.as_view(), name="brandPage" ),
    path('S-air-brands-page/',views.SAirBrandsView.as_view(), name="SairBrand"),
    path('catalogue-page/',views.CataloueView.as_view(), name="catalogue"),
    
    
    
]