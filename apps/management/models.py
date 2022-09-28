from django.db import models
import random
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=70, null=True, blank=True)
    
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.name


class Department(models.Model):
    name        = models.CharField(max_length=70,  null=False, blank=False)
    history     = models.TextField(max_length=1000, null=True,blank=True, default='No History')

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
        

    def __str__(self):
        return self.name

    
class Employee(models.Model):
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    nuban = models.CharField(max_length=10, default='0123456789')
    bank = models.CharField(max_length=25, default='First Bank Plc')
    salary = models.CharField(max_length=16,default='00,000.00')      
    def __str__(self):
        return self.first_name
        


class LEADS(models.Model):
    employee            = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)
    thumb               = models.ImageField(blank=True,     null=True)
    name                = models.CharField(max_length=50,   null=True, blank=True)
    email               = models.EmailField(null=False,     blank=False)
    address             = models.TextField(null=True,       blank=True)
    shipping_address    = models.TextField(null=True,       blank=True)
    phone               = models.CharField(max_length=15,   null=False, blank=False)
    mobile              = models.CharField(max_length=15,   null=True,  blank=True)
    fax                 = models.CharField(max_length=15,   null=False, blank=False)
    company_name        = models.CharField(max_length=50,   null=False, blank=False)
    website             = models.URLField(max_length = 200, null=False, blank=False)
    vat_numnber         = models.CharField(max_length=15,   null=False, blank=False)
    status              = models.BooleanField(default=True)
    note                = models.TextField(null=False,      blank=False)
    contents            = models.TextField(max_length=1000, null=True,blank=True, default='No contents')
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


# class Kin(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     address = models.TextField(max_length=100)
#     occupation = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=15)
#     employee = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)

#     def __str__(self):
#         return self.first_name+'-'+self.last_name
    


# class Attendance (models.Model):
#     STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
#     date = models.DateField(auto_now_add=True)
#     first_in = models.TimeField()
#     last_out = models.TimeField(null=True)
#     status = models.CharField(choices=STATUS, max_length=15 )
#     staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

#     def save(self,*args, **kwargs):
#         self.first_in = timezone.localtime()
#         super(Attendance,self).save(*args, **kwargs)
    
#     def __str__(self):
#         return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)

# class Leave (models.Model):
#     STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
#     employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
#     start = models.CharField(blank=False, max_length=15)
#     end = models.CharField(blank=False, max_length=15)
#     status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

#     def __str__(self):
#         return self.employee + ' ' + self.start

# class Recruitment(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name= models.CharField(max_length=25)
#     position = models.CharField(max_length=15)
#     email = models.EmailField(max_length=25)
#     phone = models.CharField(max_length=11)

#     def __str__(self):
#         return self.first_name +' - '+self.position