from django.contrib import admin

# Register your models here.

from .models import dish, com_ingredients, maj_ingredients

class dishAdmin(admin.ModelAdmin):
    class Meta:
        model = dish

class majAdmin(admin.ModelAdmin):
    class Meta:
        model = maj_ingredients

class comAdmin(admin.ModelAdmin):
    class Meta:
        model = com_ingredients



admin.site.register(dish,dishAdmin)
admin.site.register(maj_ingredients,majAdmin)
admin.site.register(com_ingredients,comAdmin)