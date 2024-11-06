from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..models import Category
from ..serializers.category import CategorySerializer


class CategoryView(APIView):

    def get(self, request):
        try:
            all_categories = Category.objects.all()
            serializer = CategorySerializer(all_categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "An error occurred while retrieving categories."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                new_category = serializer.save()
                return_category = CategorySerializer(new_category)
                return Response(return_category.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            # Handles validation errors from is_valid
            return Response(
                {"error": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while creating the category."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, category_id=None):
        try: 
            category_obj = Category.objects.get(category_id=category_id)
            serializer = CategorySerializer(category_obj, data=request.data)
            if serializer.is_valid():
                fully_updated_category = serializer.save()
                return_category = CategorySerializer(fully_updated_category)
                return Response(return_category.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        except ValidationError as e:
            return Response(
                {"error": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while updating the category."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, category_id=None):
        try:
            category_obj = Category.objects.get(category_id=category_id)
            serializer = CategorySerializer(category_obj, data=request.data, partial=True)
            if serializer.is_valid():
                updated_category = serializer.save()
                return_category = CategorySerializer(updated_category)
                return Response(return_category.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response(
                {"error": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An error occurred while partially updating the category."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self, request, category_id=None):
        try:
            category_obj = Category.objects.get(category_id=category_id)
            category_obj.delete()
            return Response(
                {"message": "Category deleted successfully."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error in DELETE request: {e}")
            return Response(
                {"error": "An error occurred while deleting the category."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
