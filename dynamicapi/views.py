import importlib

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DynamicApiView(APIView):

    def get(self, request, productcode=None,*args, **kwargs):
        function_string = f'dynamicapi.services.{productcode}.get_price'
        mod_name, func_name = function_string.rsplit('.',1)
        
        try:
            mod = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            return Response({'msg': f'{productcode} no pricing calculation for this product type'}, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': e}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        return getattr(mod, func_name)(request)
