from django.contrib import admin
from .models import post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(post,PostAdmin)