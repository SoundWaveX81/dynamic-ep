from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.request import Request
from rest_framework.response import Response
from dynamicapi.serializers.product_one_serializer import ProductOneSerializer


class ProductOne:

    def get_price(self, request: Request) -> Response:
        product_serializer = ProductOneSerializer(data=request.query_params)

        if product_serializer.is_valid():
            return Response({'detail': 'product one ok'}, HTTP_200_OK)
            
        return Response(product_serializer.errors, HTTP_400_BAD_REQUEST)