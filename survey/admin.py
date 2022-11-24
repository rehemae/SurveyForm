from django.contrib import admin
from survey.models import Survey


# Register your models here.

class SurveyAdmin(admin.ModelAdmin):
    list_display=('name','age','gender','phone_number','satisfied','feedback')
    search_fields=('name','age','gender','phone_number','satisfied','feedback')
admin.site.register(Survey,SurveyAdmin)




