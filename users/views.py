from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.shortcuts import render

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
# Create your views here.
