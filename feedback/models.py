from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description", null=True)
    attachment = models.FileField(blank=True, null=True)
    creation_time = models.DateTimeField(auto_created=True, auto_now=True)
    is_checked = models.BooleanField(default=False)

    def user_email(self):
        return self.user.email

    def __str__(self):
        return "Feedback about {} from user {}".format(self.title, self.user.username)



