from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Photo(models.Model):
    src = models.ImageField(upload_to='photos')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'photo'

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='id')
    writedate = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)
    photos = models.ManyToManyField(Photo, related_name='posts')  #다대다 연결
    type = models.CharField(max_length=100)
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post'
