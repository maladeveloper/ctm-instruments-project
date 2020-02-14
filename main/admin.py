from django.contrib import admin

# Register your models here.
from main.models import Instrument

#Tells django that we can manage the model through the admin site
admin.site.register(Instrument)
