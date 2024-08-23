from .serializers import InscricaoSerializer
from .models import Inscricao
from rest_framework import generics


class InscricaoListCreate(generics.ListCreateAPIView):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer


class InscricaoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer