import json
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from dynamicapi.serializers.product_one_serializer import ProductOneSerializer


def get_price(request: Request) -> Response:

    data = json.dumps(request.query_params)
    data = json.loads(data)
    product_serializer = ProductOneSerializer(data=data)

    if product_serializer.is_valid():
        return Response({'detail': 'ok'}, status.HTTP_200_OK)
        
    return Response(product_serializer.errors, status.HTTP_400_BAD_REQUEST)
