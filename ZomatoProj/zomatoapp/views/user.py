from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..models import User
from ..serializers.user import UserSerializer

class UserListView(APIView):
    def get(self, request):
        users_list = User.objects.all()
        serializers = UserSerializer(users_list, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            new_user = serializers.save()
            return_user = UserSerializer(new_user)
            return Response(return_user.data, status=status.HTTP_201_CREATED)