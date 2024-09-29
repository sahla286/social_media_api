from rest_framework import serializers
from api.models import socialmedia
from django.contrib.auth.models import User
from .models import Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
    
class LikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['user','comments','date','like_count']
    
class SocialSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True) 
    date=serializers.CharField(read_only=True)
    like=LikeUserSerializer(read_only=True,many=True)
    like_count=serializers.CharField(read_only=True)
    comments=CommentUserSerializer(read_only=True,many=True)
     
    class Meta:
        model=socialmedia
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    like=LikeUserSerializer(read_only=True,many=True)
    like_count=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'