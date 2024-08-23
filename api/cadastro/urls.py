from django.urls import path
from .views import InscricaoListCreate, InscricaoRetrieveUpdateDestroy


urlpatterns = [
    path('inscricoes/', InscricaoListCreate.as_view(), name='inscricao-list-create'),
    path('inscricoes/<int:pk>', InscricaoRetrieveUpdateDestroy.as_view(), name='inscricao-retrieve')
]