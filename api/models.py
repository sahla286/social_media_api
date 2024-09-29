from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class socialmedia(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='images',null=False)
    thought=models.CharField(max_length=500,null=True)
    like=models.ManyToManyField(User,related_name='likes')
    # comments=models.CharField(max_length=500)

    @property
    def like_count(self):
        count_like=self.like.all()
        if count_like:
            return count_like.count()
        else:
            return 0
        
    @property
    def comments(self):
        return self.comment_set.all() 

class Comment(models.Model):
    post=models.ForeignKey(socialmedia,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='like')

    @property
    def like_count(self):
        count_like=self.like.all()
        if count_like:
            return count_like.count()
        else:
            return 0
        
    @property
    def replay(self):
        return self.replaycomment_set.all() 
        
class ReplayComment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Comments=models.ForeignKey(Comment,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    replay=models.CharField(max_length=500)
    like=models.ManyToManyField(User,related_name='replay_like')

    @property
    def like_count(self):
        count_like=self.like.all()
        if count_like:
            return count_like.count()
        else:
            return 0