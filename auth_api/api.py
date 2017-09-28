from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, views
from django.contrib.auth import authenticate, login
from rest_framework.response import Response


def load_auth(request):
    return JsonResponse({"id": 1, "username": "testuser"})


class LoginView(views.APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"))
        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': ''
            }, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({'id': 0})
