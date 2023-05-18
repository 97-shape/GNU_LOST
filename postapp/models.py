from django.db.models import Min
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', models.DO_NOTHING)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # 이미지를 저장하기 전에 MySQL에 경로를 저장할 수 있도록 로직을 추가할 수 있습니다.
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'photo'

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='id')
    writedate = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)
    photos = models.ManyToManyField(Photo, related_name='posts')  #다대다 연결
    type = models.CharField(max_length=100)
    reward = models.IntegerField()

    def get_thubnail(self):
        return self.photos.first()

    class Meta:
        managed = True
        db_table = 'post'