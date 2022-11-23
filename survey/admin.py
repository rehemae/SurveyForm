from django.contrib import admin
from survey.models import Profile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','age','gender','phone_number')
    search_fields=('user','age','gender','phone_number')
admin.site.register(Profile,ProfileAdmin)

