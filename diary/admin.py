from django.contrib import admin
from .models import Milk, Kefir, Cheese, CabbageCheese
# Register your models here.


admin.site.register(Milk)
admin.site.register(Kefir)
admin.site.register(Cheese)
admin.site.register(CabbageCheese)