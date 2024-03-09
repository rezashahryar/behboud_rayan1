from rest_framework import generics
from .permissions import IsSuperUserOrReadOnly
from rest_framework.viewsets import ModelViewSet
from hamayesh.models import Hamayesh, ParticipantHamayesh
from .serializers import HamayeshSerializer, ParticipantsSerializer

# create your views here


class RegisterHamayesh(generics.ListCreateAPIView):
    queryset = ParticipantHamayesh.objects.all()
    serializer_class = ParticipantsSerializer


class HamayeshViewSet(ModelViewSet):
    queryset = Hamayesh.objects.prefetch_related('participants').all()
    serializer_class = HamayeshSerializer
    permission_classes = [IsSuperUserOrReadOnly]

