from django.contrib import admin

from .models import Action, ActionImage

class ImageInline(admin.TabularInline):
    model = ActionImage

@admin.register(Action)
class ActionManager(admin.ModelAdmin):
    inlines =[
        ImageInline,
    ]


@admin.register(ActionImage)
class ActionImageManager(admin.ModelAdmin):
    pass
