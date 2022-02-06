from os import preadv
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from API_Side.managers import MyAccountManager
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random, string
from django.contrib.auth.models import User





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def pre_save_store_receiver(sender, instance, *args, **kwargs):
    if not instance.store_link:
        instance.store_link = slugify(random_link_generator() + "-" + instance.store_name)


def upload_location(instance, filename):
    print("\n\n instance.store_name : ", instance.store_name, "\n\n")
    print("\n\n instance.store_name.owner : ", instance.store_name.owner, "\n\n")
    file_path = f'store/{str(instance.store_name.owner)}/{str(instance.store_name)}-{filename}'
    return file_path

def random_link_generator():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Account(AbstractBaseUser):
    mobile_num  = models.CharField(max_length=13, unique=True)
    first_name  = models.CharField(max_length=30, blank=True)
    last_name   = models.CharField(max_length=30, blank=True)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login	= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin	= models.BooleanField(default=False)
    is_active	= models.BooleanField(default=True)
    is_staff	= models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)


    USERNAME_FIELD = 'mobile_num'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.mobile_num

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True




class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def _str_(self):
        return self.title

class Store(models.Model):
    store_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField(max_length=5000, null=False, blank=False)
    store_link = models.SlugField(blank=True, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.store_name


pre_save.connect(pre_save_store_receiver, sender=Store)




class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    MRP = models.IntegerField()
    sale_price = models.IntegerField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    store_name = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    customer_email  = models.EmailField(max_length=17, unique=True)
    customer_name = models.CharField(max_length=50, blank=True)
    customer_address = models.TextField(max_length=5000, null=False, blank=False)

    def __str__(self):
        return self.customer_name

class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer