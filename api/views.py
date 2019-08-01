from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Item, FavoriteItem
from .serializers import ItemListSerializer, ItemDetailSerializer, UserLoginSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

# Create your views here.
# class UserLoginAPIView(APIView):
    # # serializer_class = UserLoginSerializer

    # def post(self, request):
    #     my_data = request.data
    #     serializer = UserLoginSerializer(data=my_data)
    #     if serializer.is_valid(raise_exception=True):
    #         valid_data = serializer.data
    #         return Response(valid_data, status=HTTP_200_OK)
    #     return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'description',]
	permission_classes = [AllowAny]


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated, IsOwner]

