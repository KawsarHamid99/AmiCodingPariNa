from django.contrib import admin
from .models import Payload
# Register your models here.
@admin.register(Payload)
class PayloadAdmin(admin.ModelAdmin):
    list_display=["input_value","timestamp"]