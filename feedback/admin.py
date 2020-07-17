from django.contrib import admin
from feedback.models import Feedback


# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user_id", "title", "user", "user_email",  "creation_time", "attachment", "is_checked")
    list_display_links = ("user_id", "title")
    list_editable = ["is_checked"]


admin.site.register(Feedback, FeedbackAdmin)
