from django.contrib import admin
from .models import (
				Food,
				BeautyHealth,
				ElectricalEquipment,
				AutoMoto,
				ForKids,
				ForFitness,
				HomeGarden,
				ComputerOffice,
				Highlights
				)
# Register your models here.

admin.site.register(Food)
admin.site.register(BeautyHealth)
admin.site.register(ElectricalEquipment)
admin.site.register(AutoMoto)
admin.site.register(ForKids)
admin.site.register(ForFitness)
admin.site.register(HomeGarden)
admin.site.register(ComputerOffice)
admin.site.register(Highlights)