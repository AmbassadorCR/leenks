from links.models import Link
from rest_framework import serializers

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    num_clicks = serializers.Field(source='clicks')
 
    class Meta:
        model = Link
        fields = ['id', 'title', 'url', 'num_clicks']
        read_only_fields = ['id']
