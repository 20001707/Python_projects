from django.contrib import admin
from .models import CustomUser, Package, Agent ,book

# Register your models here.

admin.site.register(Package)
admin.site.register(Agent)
admin.site.register(CustomUser)
admin.site.register(book)





