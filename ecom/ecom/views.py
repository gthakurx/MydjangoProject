from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response 

from ecom.models import Shipping_Address , User
from ecom.Serializers import UserSerializer , ShippingAddressSerializer,CreateShippingAddressSerializer

from django.shortcuts import get_object_or_404


class UserListCreateAPIView(APIView):

    # queryset=User.objects.all()
    # serializer_class= UserSerializer
    # Creating API for get and post 

    def get(self,request):
        users=User.objects.all().prefetch_related("shipping_address").select_related("default_shipping_address")
        return Response(UserSerializer(users,many=True).data)

    def post(self,request):
        serialized=UserSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors,status=400)
        serialized.save()
        return Response(serialized.data,status=201)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ShippingAddressListCreateAPIView(ListCreateAPIView):
    serializer_class=CreateShippingAddressSerializer
    def post(self, request, user_id):
        user=get_object_or_404(User,pk=user_id)
        serialized =CreateShippingAddressSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors,status=400)

        shipping_address=Shipping_Address(
            street=serialized.validated_data["street"],
            city=serialized.validated_data["city"],
            state=serialized.validated_data["state"],
            zip_code=serialized.validated_data["zip_code"],
            country=serialized.validated_data["country"],
            user=user
        )     
        shipping_address.save()

        return Response(ShippingAddressSerializer(shipping_address).data,status=201)

class   SetDefaultShippingAddress(APIView):
    def patch(self,request,user_id,address_id):

        user=get_object_or_404(User,pk=user_id)
        address=get_object_or_404(Shipping_Address,user_id=user_id,pk=address_id)
        user.default_shipping_address=address

        user.save()
        return Response(UserSerializer(user).data,200)