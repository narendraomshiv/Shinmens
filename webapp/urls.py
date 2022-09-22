from django.urls import path
from  .import views



urlpatterns = [

    path('', views.HomePageView.as_view(), name="homePage" ),
    path('brand/', views.BrandTeamplatesView.as_view(), name="brandPage" ),
    path('S-air-brands-page/',views.SAirBrandsView.as_view(), name="SairBrand"),
    path('catalogue-page/',views.CataloueView.as_view(), name="catalogue"),
    path('tech-index-page/',views.TechPageView.as_view(), name="tech"),
    path('corporate/',views.CorporateView.as_view(), name="corporate"),
    path('newspage/',views.NewsView.as_view(),name ='news'),
    path('slash-drand-details/',views.SlashBrandsView.as_view(), name ='slash'),
    path('/stx-fg/',views.StxBrandsView.as_view(), name='stxbrand'),
    path('s-heat-drand-details/',views.SheatBrandsView.as_view(),name ='sheat'),
    
    
]

