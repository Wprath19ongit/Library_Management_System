from django.contrib import admin
from .models import client_info,admin_info,books
# Register your models here.

admin.site.register(client_info)
admin.site.register(admin_info)
admin.site.register(books)