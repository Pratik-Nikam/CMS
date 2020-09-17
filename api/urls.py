from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import ContentView
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'content', views.ContentView, 'Crud')
"""
Below endpoint will help registerd user to generate Authentication Token
and to access api content
"""
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
