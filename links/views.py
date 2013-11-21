from links.models import Link
from rest_framework import viewsets
from links.serializers import LinkSerializer
from django.shortcuts import redirect
from django.http import Http404  

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

def redirectView(request):
	linkQuery = Link.objects.filter(title=request.path[3:])

	if linkQuery.exists():
		link = linkQuery.first();
		link.clicks += 1;
		link.save();
		return redirect('/static/Leenks.html?link=' + link.title)
	else:
		raise Http404

	

	

