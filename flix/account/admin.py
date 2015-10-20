# Django
from django.contrib import admin

# Local
from .models import ViewerProfile, ViewEvent

class ViewerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_child', 'created_at', 'updated_at')

class ViewEventAdmin(admin.ModelAdmin):
    list_display = ('viewer_profile', 'created_at', 'updated_at')

admin.site.register(ViewerProfile, ViewerProfileAdmin)
admin.site.register(ViewEvent, ViewEventAdmin)
