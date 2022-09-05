from django.urls import path
from . import views

#======#
urlpatterns = [
    path('', views.adminPanel, name="dashboardHome"),
    path('admin-login', views.login, name="loginAdmin"),
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
    
    
    
    
]