from django.contrib import admin
from survey.models import Profile,Question,Choice,Feedback


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('first_name','age','gender','phone_number')
    search_fields=('user','age','gender','phone_number')
admin.site.register(Profile,ProfileAdmin)


# class QuestionAdmin(admin.ModelAdmin):
#     list_display=('question','pub_date')
#     search_fields=('question','pub_date')
# admin.site.register(Question,QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display=('question','choice')
    search_fields=('question','choice')
admin.site.register(Choice,ChoiceAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display=['text']
    search_fields=['text']
admin.site.register(Feedback,FeedbackAdmin)


