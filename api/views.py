from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from farming_v3.models import Tanaman, Panenan, PestisidaPupuk, Hama

import json

from farming_v3.serializers import TanamanSerializer, PanenanSerializer, HamaSerializer, PestisidaPupukSerializer

# @api_view(["POST", "GET"])
# def api_home(request, *args, **kwargs):
#     '''
#     DRF API View
#     '''
    
#     serializer = TanamanSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         print(serializer.data)
#         return Response(serializer.data)
    
#     return Response({"invalid" : "not good data"}, status=400)