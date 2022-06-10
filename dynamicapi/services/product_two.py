import json
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from dynamicapi.serializers.product_two_serializer import ProductTwoSerializer



def get_price(request: Request) -> Response:

    product_serializer = ProductTwoSerializer(data=request.query_params)

    if product_serializer.is_valid():
        return Response({'detail': 'ok'}, status.HTTP_200_OK)
        
    return Response(product_serializer.errors, status.HTTP_400_BAD_REQUEST)
