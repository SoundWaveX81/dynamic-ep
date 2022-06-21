from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.request import Request
from rest_framework.response import Response
from dynamicapi.serializers.product_two_serializer import ProductTwoSerializer

class ProductTwo:

    def get_price(self, request: Request) -> Response:
        product_serializer = ProductTwoSerializer(data=request.query_params)

        if product_serializer.is_valid():
            return Response({'detail': 'ok product type'}, HTTP_200_OK)
            
        return Response(product_serializer.errors, HTTP_400_BAD_REQUEST)
