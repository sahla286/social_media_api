from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter 
from rest_framework.authtoken.views import ObtainAuthToken 

router=DefaultRouter()
router.register('users',views.UserViewsetView,basename='users')
router.register('postimage',views.SocialViewSet,basename='postimage')
router.register('like',views.LikeViewSet,basename='like')
router.register('allpost',views.AllSocialViewSet,basename='allpost')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token',ObtainAuthToken.as_view()),
] + router.urls
