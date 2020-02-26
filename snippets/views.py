from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    Lists all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
