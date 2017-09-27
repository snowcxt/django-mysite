from rest_framework.generics import ListAPIView
from .serializers import QuestionSerializer
from .models import Question
from django.http import JsonResponse


class QuestionApi(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def load_auth(request):
    return JsonResponse({ "id": 1, "username": "testuser" })
