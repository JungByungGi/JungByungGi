from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True) # 사용자 아이디
    password = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_id = models.CharField(max_length=20) # 사용자 프로필 아이디(별칭)

    class Meta:
        db_table = 'dropbox_user'
