from rest_framework.generics import ListAPIView
from .serializers import QuestionSerializer
from .models import Question


class QuestionApi(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
