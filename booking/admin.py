from django.contrib import admin
from .models import *


admin.site.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'day', 'time', 'time_ordered')
    search_fields = ['user', 'day']
    list_filter = ('service', 'day')
