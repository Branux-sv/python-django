from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives your the most control over you appplication logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})



