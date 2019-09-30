from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Service)
admin.site.register(Price)
admin.site.register(Profile)
admin.site.register(UserService)
admin.site.register(Ad)
admin.site.register(Seat)