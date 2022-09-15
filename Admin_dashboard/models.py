from contextlib import nullcontext
from email.policy import default
from operator import truediv
from tokenize import blank_re

from django.db import models
from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.views import View


########## Custom Model manager ########
class CustomUserManager(BaseUserManager):
    def create_user(self ,username, email , phone_number, password):
        if not email:
            raise ValueError('The Email must be Set')
        if not username:
            raise ValueError("User Must have a username ")  
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username,phone_number,password):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            phone_number = phone_number,
            password = password, 
        )
        user.is_admin = True
        user.is_superuser = True
       
        user.save(using = self._db)
        return user    

############ Custom User Model ###########
class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(verbose_name = 'Email',max_length=255,unique=True)
    phone_number = models.CharField(max_length = 15, unique=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number']
    def __str__(self):
      return self.email
    def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin
    def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

    @property
    def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class SlidersImagesModel(models.Model):
  image = models.ImageField(null=True, blank=True,default='image')
  
  
class HomeBrandHeadingsModel(models.Model):
  headings = models.CharField(max_length=350, null=True, blank=True)
  description = models.CharField(max_length=500, null=True, blank=True) 
  other_description = models.CharField(max_length=500, null=True, blank=True) 



class BrandsModel(models.Model):
  image = models.ImageField(null=True, blank=True, default='image')
  headings = models.CharField(max_length=350, null=True, blank=True)
  description = models.CharField(max_length=500, null=True, blank=True) 
  other_description = models.CharField(max_length=500, null=True, blank=True) 




class ContactModels(models.Model):
  address = models.CharField(max_length=250)
  email = models.EmailField(verbose_name = 'Email',max_length=255,unique=True)
  link_in = models.URLField()




class CatalogModel(models.Model):
  image = models.ImageField(blank = True, null = True, default='image')
  years = models.CharField(max_length=20, blank = True, null = True)
  Heading = models.CharField(max_length=100, blank = True, null = True)


class TechPageModel(models.Model):
  image = models.ImageField(blank=True, null= True, default='image')
  heading = models.CharField(max_length=200, null= True, blank=True)
  title = models.CharField(max_length=200, null= True, blank=True)
  description = models.TextField(max_length=250, null=True ,blank=True)



class CorporateModel(models.Model):
  heading = models.CharField(max_length=250,null=True, blank=True)
  description = models.CharField(max_length=250,null=True, blank=True)

 
class SAirModel(models.Model):
  image = models.ImageField(blank= True, null= True, default='image')
  seriesname = models.CharField(max_length=250,null=True, blank=True)
  seriesnumber = models.IntegerField(null=True, blank=True)

class NewsModel(models.Model):
  heading = models.CharField(max_length=250,null=True, blank=True)
  title = models.CharField(max_length=100, null=True , blank=True)
  image = models.ImageField(blank= True, null= True, default='image')
  date = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)

