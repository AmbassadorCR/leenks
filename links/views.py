from links.models import Link
from rest_framework import viewsets
from links.serializers import LinkSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


