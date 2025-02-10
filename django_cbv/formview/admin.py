from django.contrib import admin
from .models import Trial


class SlugModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Trial, SlugModel)
# Register your models here.
