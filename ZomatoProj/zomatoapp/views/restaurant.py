from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from ..models import Restaurant
from ..serializers.restaurant import RestaurantSerializer


class RestaurantView(APIView):
    def get(self, request, restaurant_id=None):
        if restaurant_id:
            try:
                restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
                serializer = RestaurantSerializer(restaurant)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Restaurant.DoesNotExist:
                return Response(
                    {"error": "Restaurant not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            try:
                # Fetch all restaurants
                restaurants = Restaurant.objects.all()
                serializer = RestaurantSerializer(restaurants, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response(
                    {"error": "An error occurred while retrieving Restaurants."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

    def post(self, request):
        try:
            serializers = RestaurantSerializer(data=request.data)
            if serializers.is_valid():
                new_restaurant = serializers.save()
                return_restaurant = RestaurantSerializer(new_restaurant)
                return Response(return_restaurant.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": "An error occurred while creating the Restaurant."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, restaurant_id=None):
        try:
            restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
            serializer = RestaurantSerializer(restaurant, data=request.data)
            if serializer.is_valid():
                fully_updated_restaurant = serializer.save()
                return_restaurant = RestaurantSerializer(fully_updated_restaurant)
                return Response(return_restaurant.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Restaurant.DoesNotExist:
            return Response(
                {"error": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": "An error occurred while updating the Restaurant."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, restaurant_id=None):
        try:
            restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
            serializer = RestaurantSerializer(
                restaurant, data=request.data, partial=True
            )
            if serializer.is_valid():
                updated_restaurant = serializer.save()
                return_restaurant = RestaurantSerializer(updated_restaurant)
                return Response(return_restaurant.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Restaurant.DoesNotExist:
            return Response(
                {"error": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": "An error occurred while partially updating the Restaurant."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, restaurant_id=None):
        try:
            restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
            restaurant.delete()
            return Response(
                {"message": "Restaurant deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )

        except Restaurant.DoesNotExist:
            return Response(
                {"error": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"error": "An error occurred while deleting the Restaurant."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
