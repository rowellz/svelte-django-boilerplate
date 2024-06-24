
from django.contrib import admin
from .models import DjangoAppModel
# Register your models here.


class DjangoAdmin(admin.ModelAdmin):
    list_display = ('entry', 'user')
    list_display_links = ('entry', 'user')
    search_fields = ('entry', 'user')
    list_per_page = 25
    list_filter = ('entry', 'user')


admin.site.register(DjangoAppModel, DjangoAdmin)
