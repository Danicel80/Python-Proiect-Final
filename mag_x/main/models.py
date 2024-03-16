from django.db import models


# Create your models here.
class About(models.Model):
    about_text_id = models.AutoField(primary_key=True)
    about_text_name = models.CharField(max_length=30)
    about_text_txt = models.TextField()


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_text_name = models.CharField(max_length=30)
    contact_text_txt = models.TextField()


class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_brand = models.CharField(max_length=30)
    prod_model = models.CharField(max_length=30)
    prod_price = models.IntegerField()
    prod_img = models.CharField(max_length=30)


class ClientProd(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    client_pref = models.TextField()
    client_bas = models.TextField()
