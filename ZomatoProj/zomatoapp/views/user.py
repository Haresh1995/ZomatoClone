from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import User
from ..serializers.user import UserSerializer

class UserListView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        users_list = User.objects.all()
        serializers = UserSerializer(users_list, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request)
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            return_user = UserSerializer(new_user)
            return Response(return_user.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)