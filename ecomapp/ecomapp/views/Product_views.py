from rest_framework.response import Response
from rest_framework.views import APIView

from ecomapp.models.Product import Product, DairyProduct
from ecomapp.serializers.Product_serializer import ProductSerializer, DairyProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class ListCreateProductAPIView(APIView):

    def get(self, request):
        # products = Product.objects.all().filter(price__gte=0)#django filter have lots of attribute to
        #filter the request
        # products = Product.objects.all().filter(price__in=[0,10000000])
        products=Product.objects.raw("select * from ecomapp_Product where price > 0")#we have to specify app<name>_model name   1`
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data,status=201)

    def post(self, request):
        data = request.data
        # product = Product() we can do like this but we will need serializer here since that is correct way of converting the
        # django Model Instances to Python data types which can be rendered to Jason data types
        # product.name = data['name']
        # product.price = data['price']
        # product.description = data['description']
        # return Response({"product": product})

        decoded_data=ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response({"error": decoded_data.errors},status=400)
        decoded_data.save()
        return Response({"data":decoded_data.data},status=201)



class DairyProductListCreateApiView(ListCreateAPIView):
    queryset = DairyProduct.objects.all()
    serializer_class = DairyProductSerializer

class DairyProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DairyProduct.objects.all()
    serializer_class = DairyProductSerializer