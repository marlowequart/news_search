from django.contrib import admin

# Register your models here.

from .models import Service, Story, StoryUpdate

admin.site.register(Service)
admin.site.register(Story)
admin.site.register(StoryUpdate)