from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from api.serializers import UserSerializer,SocialSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import socialmedia
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import serializers

# Create your views here.

class UserViewsetView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class SocialViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=SocialSerializer
    queryset=socialmedia.objects.all()

    def create(self,request,*args,**kwargs):
        user=request.user
        ser=SocialSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=user)
            return Response(data=ser.data,status=status.HTTP_201_CREATED)
        return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,*args,**kw):
        id=kw.get('pk')
        post=self.queryset.get(id=id)
        if post.user==request.user:
            ser=SocialSerializer(post,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(data=ser.data,status=status.HTTP_200_OK)
            return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
             raise serializers.ValidationError('not allowed')

    def destroy(self,request,*args,**kw):
        id=kw.get('pk')
        post=self.queryset.get(id=id)
        if post.user==request.user:
            post.delete()
            return Response(data={'msg':'post deleted'},status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError('not allowed')
        
    def list(self,request,*args,**kw):
        user=self.queryset.filter(user=request.user)
        ser=self.serializer_class(user, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK) 
        
class AllSocialViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=SocialSerializer
    queryset=socialmedia.objects.all()
        
    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    def delete(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
           
    
class LikeViewSet(ModelViewSet):
    serializer_class=SocialSerializer
    queryset=socialmedia.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    def delete(self, request, *args, **kwargs):
        raise serializers.ValidationError("method is not allowed!!")
    
    @action(methods=['POST'],detail=True)
    def add_like(self,request,*args,**kw):
        id=kw.get('pk')
        likes=self.queryset.get(id=id)
        user=request.user
        likes.like.add(user)
        return Response(data={'msg':'post liked'},status=status.HTTP_200_OK)
    
    @action(methods=['DELETE'],detail=True)
    def remove_like(self,request,*args,**kw):
        id=kw.get('pk')
        likes=self.queryset.get(id=id)
        user=request.user
        likes.like.remove(user)
        return Response(data={'msg':'unliked'},status=status.HTTP_200_OK)
        
