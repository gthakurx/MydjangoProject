from rest_framework.serializers import ModelSerializer
from ecom.models import User, Shipping_Address

class CreateShippingAddressSerializer(ModelSerializer):

    class Meta:
        model=Shipping_Address
        fields=["street",'city','state','zip_code','country']

class ShippingAddressSerializer(ModelSerializer):

    class Meta:
        model=Shipping_Address
        fields="__all__"

class UserSerializer(ModelSerializer):
    shipping_address=ShippingAddressSerializer(many=True,read_only=True)
    class Meta:
        model=User
        fields="__all__"