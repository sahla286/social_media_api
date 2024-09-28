from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class socialmedia(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='images',null=True)
    thought=models.CharField(max_length=500,null=True)
    like=models.ManyToManyField(User,related_name='likes')

    @property
    def like_count(self):
        count_like=self.like.all()
        if count_like:
            return count_like.count()
        else:
            return 0