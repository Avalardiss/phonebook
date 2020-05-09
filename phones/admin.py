from django.contrib import admin

from.models import Abonent

class AbonentAdmin(admin.ModelAdmin):
	list_display = ("id", "rank", "name", "phone", "IP_phone")

admin.site.register(Abonent, AbonentAdmin)