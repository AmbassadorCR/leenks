from links.models import Link
from rest_framework import serializers

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['title']
