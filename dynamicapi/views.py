from .services import *

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView


class DynamicApiView(APIView):

    def __product_type_class_factory(self, class_name: str):
        product_type_classes = {
            'ProductOne': ProductOne,
            'ProductTwo': ProductTwo
        }
        return product_type_classes[class_name]

    def get(self, request, productcode:str = None, *args, **kwargs):
        try:
            new_obj= self.__product_type_class_factory(productcode)()
        except KeyError as e:
            return Response({'msg': 'this product does not exist'}, HTTP_400_BAD_REQUEST)
        except NameError as e:
            return Response({'msg': 'math for this product does not exist'}, HTTP_500_INTERNAL_SERVER_ERROR)

        return new_obj.get_price(request)