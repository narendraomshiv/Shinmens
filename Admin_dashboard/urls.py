from ast import Delete
from django.urls import path

from . import views

#======#
urlpatterns = [
    path('', views.adminPanel, name="dashboardHome"),
    path('admin-login', views.Login.as_view(), name="loginAdmin"),
    path('user-logout/', views.userlogout, name ='logouts'),
    path('admin-dashboard/delete-user/<int:id>', views.deleteUser, name="deleteUser" ),
    path('admin-add-user', views.AddUser, name="addUser" ),
    path('admin-profile-user', views.profile, name="profileUser" ),
    path('update-user-profile/<int:id>', views.UpdateUserProfileView, name="editUser"),
    path('user-details/',views.ShowUserView.as_view(), name="showUser"),
    path('sliders-images-details/',views.SlidersImagesDetailsView.as_view(), name="showDetails"),
    
    path('add-sliders-images', views.SlidersImagesView.as_view(), name="addSliders"),
    path('edit-sliders-images/<int:id>', views.EditSliderImagesView.as_view(), name="editSlidersImages"),
    path('sliders-images-delete/<int:id>', views.DeleteSlidersImagesView.as_view(), name="DeleteSlidersImages"),
    path('add-new-brands', views.AddBrandView.as_view(), name="addBrand"),
    path('brands-details/',views.BrandsDetailsView.as_view(), name="brandDetails"),
    path('add-new-catalogue', views.AddCatalogueViews.as_view(), name="addCatalogue"),
    path('catalogue-lists-details/',views.CatalagueListDetailsView.as_view(), name="catalogueDetails"),
    path('edit-catalogue/<int:id>',views.EditCatalogueView.as_view(), name ="editCatalogue"),
    path('delete-catalog/<int:id>',views.DeleteCatalogView.as_view(),name = 'dalatecatalog'),
    path('add-tech/',views.AddTechView.as_view(),name='addTech'),
    path('all-tech-details/',views.TechListDetailsView.as_view(),name='techDetails'),
    path('edit-tech/<int:id>',views.EditTechView.as_view(),name='edittech'),
    path('delete-tech/<int:id>',views.DeleteTechView.as_view(),name='techDelete'),
    path('add-new/',views.AddNewsViews.as_view(),name='addnews'),
    path('all-news-details/',views.NewsDetailsView.as_view(),name='newsDetails'),
    path('edit-news/<int:id>',views.EditNewsView.as_view(),name='editNews'),
    path('delete-news/<int:id>',views.DeleteNewsviews.as_view(),name='newsDelete'),
  
    
    
    
    
    
    

    
]