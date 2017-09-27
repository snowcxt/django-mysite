from django.shortcuts import render
from django.http import JsonResponse

def load_auth(request):
    return JsonResponse({ "id": 1, "username": "testuser" })
