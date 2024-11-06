from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
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
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle any other unexpected errors
            print(f"Error in POST request: {e}")
            return Response(
                {"error": "An error occurred while creating the user."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, user_id=None):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                fully_updated_user = serializer.save()
                return_user = UserSerializer(fully_updated_user)
                return Response(return_user.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error in PUT request: {e}")
            return Response(
                {"error": "An error occurred while updating the user."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, user_id=None):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                updated_user = serializer.save()
                return_user = UserSerializer(updated_user)
                return Response(return_user.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error in PATCH request: {e}")
            return Response(
                {"error": "An error occurred while partially updating the user."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, user_id=None):
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return Response(
                {"message": "User deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )

        except User.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error in DELETE request: {e}")
            return Response(
                {"error": "An error occurred while deleting the user."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
