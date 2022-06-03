from django.contrib import admin
from .models import Image,Profile,Likes,Comments

admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields=('name','image','caption','profile','profile_detail')
    list_display = ('name','image','caption','posted')
    list_filter = ('posted',)
    search_fields = ('name',)
    ordering = ('posted',)

