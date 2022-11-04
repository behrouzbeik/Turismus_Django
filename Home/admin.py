from django.contrib import admin

from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    pass

class StateAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass

class TerminalAdmin(admin.ModelAdmin):
    pass

class TransportCoAdmin(admin.ModelAdmin):
    pass

class ExtraditionAdmin(admin.ModelAdmin):
    pass

class TransportAdmin(admin.ModelAdmin):
    pass

class ResidenceAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class TourAdmin(admin.ModelAdmin):
    pass

class MyCompanyInfoAdmin(admin.ModelAdmin):
    pass



admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(TransportCo, TransportCoAdmin)
admin.site.register(Extradition, ExtraditionAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Residence, ResidenceAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(MyCompanyInfo, MyCompanyInfoAdmin)
