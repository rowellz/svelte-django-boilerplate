
from django.contrib import admin
from .models import ChefyRecipeModel
# Register your models here.


class ChefyAdmin(admin.ModelAdmin):
    list_display = ('chat_gpt_response', 'user')
    list_display_links = ('chat_gpt_response', 'user')
    search_fields = ('chat_gpt_response', 'user')
    list_per_page = 25
    list_filter = ('chat_gpt_response', 'user')


admin.site.register(ChefyRecipeModel, ChefyAdmin)
