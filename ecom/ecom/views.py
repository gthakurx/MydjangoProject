from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response 

from ecom.models import Shipping_Address , User
from ecom.Serializers import UserSerializer , ShippingAddressSerializer,CreateShippingAddressSerializer

from django.shortcuts import get_object_or_404


class UserListCreateAPIView(ListCreateAPIView):

    queryset=User.objects.all()
    serializer_class= UserSerializer

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