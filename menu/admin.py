from django.contrib import admin
from .models import Menu, MenuEntity, SubMenuEntity
# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuEntity)
admin.site.register(SubMenuEntity)