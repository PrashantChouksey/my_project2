from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_per_page = 25
    search_fields = ('name', 'email')

admin.site.register(Realtor, RealtorAdmin)