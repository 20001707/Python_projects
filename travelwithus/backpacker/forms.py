from django import forms
from .models import Package, CustomUser ,Agent
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



class DateInput(forms.DateInput):
    input_type = 'date'



class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        exclude = ['users','agent']
       
        widgets = {
            'ddate': DateInput()
        }
   

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','email','phone','aadhar_no','aadhar_image',]
        
    @transaction.atomic
    def save(self):
        customuser = super().save(commit=False)
        customuser.is_customer=True
        customuser.save()
        return customuser

class AgentSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','email',]
        
    @transaction.atomic
    def save(self):
        customuser = super().save(commit=False)
        customuser.is_agent=True
        customuser.save()
        return customuser

class AgentDetailForm(forms.ModelForm):
    

    class Meta:
        model = Agent
        fields = '__all__'
        exclude = ['User']

    