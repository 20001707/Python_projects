from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
import datetime


class CustomUser(AbstractUser):
    is_agent = models.BooleanField('agent stat', default=False)
    is_customer = models.BooleanField('customer status', default=False)
    phone = models.CharField(max_length=10,default="")
    aadhar_no = models.CharField(max_length=12,default="")
    aadhar_image=models.ImageField(default="B.png")
    REQUIRED_FIELDS = []


class Agent(models.Model):
    User = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


Travel_mode = (
    ('T', 'Train'),
    ('B', 'Bus'),
    ('F', 'Flight'),
)


# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    cost = models.IntegerField()
    duration = models.IntegerField()
    Location = models.CharField(max_length=100)
    ddate = models.DateField(
        validators=[MinValueValidator(datetime.date.today)])
    posteddate = models.DateField(auto_now=True)
    dloc = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    slots = models.IntegerField(default=2)
    image = models.ImageField(default="B.png")
    users = models.ManyToManyField(
        CustomUser, related_name='participants', blank=True)
    mode = models.CharField(max_length=1, choices=Travel_mode,default="B")

    class Meta:
        ordering = ['-posteddate']

    def __str__(self):
        return self.title


class book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE,)
    time = models.DateField(auto_now=True)
    price = models.IntegerField()
    nos = models.IntegerField(default=1)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    boarding=models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        ordering = ['-time']
