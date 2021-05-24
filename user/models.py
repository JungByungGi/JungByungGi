from django.db import models


# Create your models here.
class DropboxUser(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    registered_dttm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'dropbox_user'
