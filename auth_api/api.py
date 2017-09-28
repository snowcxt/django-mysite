from django.http import JsonResponse, HttpResponse
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


def load_auth_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"id": request.user.id, "username":  request.user.username})
    else:
        return HttpResponse('')


@csrf_exempt
def login_view(request):
    user = authenticate(
        username=request.POST.get("username"),
        password=request.POST.get("password"))
    if user is None or not user.is_active:
        return JsonResponse({
            'status': 'Unauthorized',
        }, status=status.HTTP_401_UNAUTHORIZED)
    login(request, user)
    return JsonResponse({'id': user.id, 'username': user.username})


def logout_view(request):
    logout(request)
    return HttpResponse('')
