from multiprocessing import AuthenticationError
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import isAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class OfferViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.OfferSerializer
    queryset = models.Offer.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)