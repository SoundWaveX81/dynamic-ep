from .services import *

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class DynamicApiView(APIView):

    def __product_type_class_factory(self, class_name: str):
        classes = {
            'ProductOne': ProductOne,
            'ProductTwo': ProductTwo
        }
        return classes[class_name]

    def get(self, request, productcode=None, *args, **kwargs):
        try:
            new_obj= self.__product_type_class_factory(productcode)()
        except KeyError as e:
            return Response({'msg': 'math this product does not exist'}, HTTP_400_BAD_REQUEST)

        return new_obj.get_price(request)