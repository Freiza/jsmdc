from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100,unique=True)
    firm_name = models.CharField(max_length=100)
    firm_type = models.CharField(max_length=100)
    PAN = models.CharField(max_length=100)
    GST = models.CharField(max_length=100)
    authorized_person_firstname = models.CharField(max_length=100)
    authorized_person_lastname = models.CharField(max_length=100)
    deposit = models.IntegerField(blank=True,null=True)
    
    
    
    
    registered_address_of_company = models.CharField(max_length=1000)
    
    email_id = models.CharField(max_length=100,blank=True)
    email_id_of_autherized_person = models.CharField(max_length=100,blank=True)
    mobile_number = models.CharField(max_length=100)
    jadmin = models.ForeignKey("JAdmin",on_delete=models.CASCADE,default=1)
    password = models.CharField(max_length=100)
    vghat = models.ManyToManyField('Sandghat')

    class Meta:
        verbose_name = "Vendor"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LeadFile(models.Model):
    authority_letter = models.FileField(blank=True)
    pan_photo = models.FileField(blank=True)
    client_credential_file = models.FileField(blank=True)
    gst_document = models.FileField(blank=True)
    photo_of_authorized_person = models.FileField(blank=True)
    leader = models.ForeignKey("Lead",on_delete=models.CASCADE,default=1)


class Sandghat(models.Model):
    sno = models.IntegerField(default=0)
    mauza = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area = models.FloatField()
    qtycft = models.IntegerField(default=0)
    emd = models.FloatField()
    

    def __str__(self):
        return f"{self.mauza}:{self.location}:{self.qtycft}"

class JAdmin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.email
