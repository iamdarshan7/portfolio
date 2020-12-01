from django.contrib import admin
from .models import Portfolio1, Portfolio2, ContactInfo
# Register your models here.

admin.site.register(Portfolio1)
admin.site.register(Portfolio2)
# admin.site.register(ContactInfo)

@admin.register(ContactInfo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']