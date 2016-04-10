from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from api_auth.api.models import *

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from .decorators import render_to
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)


@render_to('home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return context()


@login_required
@render_to('home.html')
def done(request):
    """Login complete view, displays user data"""
    conn = context()
    response_data = {}
    response_data['backend'] = "backend: google"
    response_data['token'] = 'token:' + request.user.token
    response_data['is_new'] = 'is_new:' + str(request.user.is_new)
    response_data['first_name'] = 'first_name:' + request.user.first_name
    response_data['last_name'] = 'last_name:' + request.user.last_name
    response_data['email'] = 'email:' + request.user.email
    HttpResponse(response_data, content_type="application/json")
    return conn


class AuthView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({'detail': "I suppose you are authenticated"})
