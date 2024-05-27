from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer


class UserListCreateApiView(APIView):

    def get(self, request):
        print(request.headers)
        users = User.objects.all()
        serialized=UserSerializer(users, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized=UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)