from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import User
from ..serializers.user import UserSerializer

class UserListView(APIView):
    def get(self, request):
        try:
            users_list = User.objects.all()
            serializers = UserSerializer(users_list, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "An error occurred while retrieving users."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                new_user = serializer.save()
                return_user = UserSerializer(new_user)
                return Response(return_user.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            # Handles validation errors from is_valid
            return Response(
                {"error": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Handle any other unexpected errors
            print(f"Error in POST request: {e}")
            return Response(
                {"error": "An error occurred while creating the user."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )