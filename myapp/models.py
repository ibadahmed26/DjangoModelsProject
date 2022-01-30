from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    name = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    date = models.DateField()

    class Meta:
        abstract = True


class Page(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='mypage')


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, related_name='mypost')


class Song(BaseModel):
    user = models.ManyToManyField(User)
    duration = models.IntegerField()

    def get_singers(self):
        return " ".join([str(i) for i in self.user.all()])
