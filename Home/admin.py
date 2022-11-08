from django.contrib import admin

from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    pass

class StateAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    list_display = ['state','city','image' , 'home_page_display' , 'short_description']
    # inlines = [city,image]
    list_editable = ('home_page_display',)
    

class TerminalAdmin(admin.ModelAdmin):
    pass

class TransportCoAdmin(admin.ModelAdmin):
    pass

class ExtraditionAdmin(admin.ModelAdmin):
    pass

class TransportAdmin(admin.ModelAdmin):
    pass

class ResidenceAdmin(admin.ModelAdmin):
    list_display = ['name','city','logo' , 'telnum' , 'graid_star']
    # inlines = [city,image]
    list_editable = ('graid_star',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['residence','adultprice','childprice' , 'babyprice' , 'buyscore', 'capacity']
    # inlines = [ResidenceAdmin]
    list_editable = ('adultprice','childprice' , 'babyprice' , 'buyscore', 'capacity')

class TourAdmin(admin.ModelAdmin):
    list_display = ['name','hotel','price' , 'discount' , 'buyscore', 'capacity', 'home_page_display']
    # inlines = [city,image]
    list_editable = ('home_page_display', 'capacity')
    

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
