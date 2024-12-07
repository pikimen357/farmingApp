# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
# from farming.models import Petani, Panenan, Tanaman, Hama, PestisidaPupuk
# from farming.serializers import PetaniSerializer, PanenanSerializer, TanamanSerializer, HamaSerializer, PestisidaPupukSerializer

# @api_view(['GET', 'POST'])
# def petani_list(request, format=None):
    
#     """
#     List all petani, or create a new petani.
#     """
    
#     if request.method == 'GET':
#         petani = Petani.objects.all()
#         serializer = PetaniSerializer(petani, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PetaniSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'POST'])
# def panenan_list(request, format=None):
    
#     if request.method == 'GET':
#         panenan = Panenan.objects.all()
#         serializer = PanenanSerializer(panenan, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
        
#         data = JSONParser().parse(request)
#         serializer = PanenanSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def tanaman_list(request, format=None):
    
#     if request.method == 'GET':
#         # ambil semua tanaman
#         tanaman = Tanaman.objects.all() 
        
#         # serializerkan data
#         serializer = TanamanSerializer(tanaman, many=True)
        
#         # kembalikan dalam bentuk json
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
        
#         # ambil data dari request
#         data = JSONParser().parse(request)
        
#         # serializerkan data
#         serializer = TanamanSerializer(data=data)
        
#         # jika valid maka disimpan jika tidak kembalikan HTTP 400
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def hama_list(request, format=None):
    
#     """
#     List all hama, or create a new hama.
#     """
    
#     if request.method == 'GET':
#         hama = Hama.objects.all()
#         serializer = HamaSerializer(hama, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = HamaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def pupuk_pestisida_list(request, format=None):
    
#     """
#     List all pupuk pestisida, or create a new pupuk pestisida.
#     """
    
#     if request.method == 'GET':
#         pupes = PestisidaPupuk.objects.all()
#         serializer = PestisidaPupukSerializer(pupes, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PestisidaPupukSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
# @api_view(['GET', 'PUT', 'DELETE'])
# def petani_detail(request, username, format=None):
#     """
#     Retrieve, update or delete a code petani
#     """
#     try:
#         # coba ambil petani dengan id pk
#         petani = Petani.objects.get(username=username)
#     except Petani.DoesNotExist:
        
#         # jika tidak ada kembalikan HTTP 404
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PetaniSerializer(petani)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         # serializer = PetaniSerializer(petani, data=data)
#         serializer = PetaniSerializer(petani, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     elif request.method == 'DELETE':
#         petani.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def tanaman_detail(request, pk, format=None):
    
#     """
#     Retrieve, update or delete a code tanaman
#     """
    
#     try:
#         tanaman = Tanaman.objects.get(pk=pk)
#     except Tanaman.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = TanamanSerializer(tanaman)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         # serializer = TanamanSerializer(tanaman, data=data)
#         serializer = TanamanSerializer(tanaman, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         tanaman.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def panenan_detail(request, pk, format=None):
    
#     """
#     Retrieve, update or delete a code tanaman
#     """
    
#     try:
#         panenan = Panenan.objects.get(pk=pk)
#     except Panenan.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PanenanSerializer(panenan)
#         return JsonResponse(serializer.data)
    
   
    
#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         # serializer = PanenanSerializer(panenan, data=data)
#         serializer = PanenanSerializer(panenan, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # TIDAK BOLEH MENGHAPUS PANENAN !!
     
    # elif request.method == 'DELETE':
    #     panenan.delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT)


from farming.models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan
from farming.serializers import PetaniSerializer, PanenanSerializer, HamaSerializer, TanamanSerializer, PestisidaPupukSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PetaniList(APIView):
    """
    List all petani, or create a new petani.
    """
    
    def get(self, request, fromat=None):
        petani = Petani.objects.all()
        serializer = PetaniSerializer(petani, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PetaniSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PanenanList(APIView):
    """
    List all panenan, or create a new panenan.
    """
    
    def get(self, request, fromat=None):
        panenan = Panenan.objects.all()
        serializer = PanenanSerializer(panenan, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PanenanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TanamanList(APIView):
    """
    List all tanaman, or create a new tanaman.
    """
    
    def get(self, request, fromat=None):
        tanaman = Tanaman.objects.all()
        serializer = TanamanSerializer(tanaman, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TanamanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HamaList(APIView):
    """
    List all hama, or create a new hama.
    """
    
    def get(self, request, fromat=None):
        hama = Hama.objects.all()
        serializer = HamaSerializer(hama, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HamaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class PestisidaPupukList(APIView):
    """
    List all pestisida/pupuk, or create a new pestisida/pupuk.
    """
    
    def get(self, request, fromat=None):
        pupes = PestisidaPupuk.objects.all()
        serializer = PestisidaPupukSerializer(pupes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PestisidaPupukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

# DETAIL

class PetaniDetail(APIView):
    """
    Retrieve, update or delete a petani instance
    """
    
    def get_object(self, username):
        try:
            return Petani.objects.get(username=username)
        except Petani.DoesNotExist:
            return Http404
        
    def get(self, request, username, format=None):
        petani = self.get_object(username)
        serialzer = PetaniSerializer(petani)
        return Response(serialzer.data)
    
    def put(self, request, username, format=None):
        petani = self.get_object(username)
        serializer = PetaniSerializer(petani, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, username, format=None):
        petani = self.get_object(username)
        petani.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PanenanDetail(APIView):
    """
    Retrieve, update or delete a panenan instance
    """
    
    def get_object(self, pk):
        try:
            return Panenan.objects.get(pk=pk)
        except Panenan.DoesNotExist:
            return Http404
        
    def get(self, request, pk, format=None):
        panenan = self.get_object(pk)
        serialzer = PanenanSerializer(panenan)
        return Response(serialzer.data)
    
    def put(self, request, pk, format=None):
        panenan = self.get_object(pk)
        serializer = PanenanSerializer(panenan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # RIWAYAT PANENAN TIDAK BOLEH DIHAPUS
    # def delete(self, request, pk, format=None):
    #     panenan = self.get_object(pk)
    #     panenan.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
class PupukPestisidaDetail(APIView):
    """
    Retrieve, update or delete a pupuk pestisida instance
    """
    
    def get_object(self, nama_obat):
        try:
            return PestisidaPupuk.objects.get(nama_obat=nama_obat)
        except PestisidaPupuk.DoesNotExist:
            return Http404
        
    def get(self, request, nama_obat, format=None):
        pupes = self.get_object(nama_obat)
        serialzer = PestisidaPupuk(pupes)
        return Response(serialzer.data)
    
    def put(self, request, nama_obat, format=None):
        pupes = self.get_object(nama_obat)
        serializer = PestisidaPupuk(pupes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, nama_obat, format=None):
        pupes = self.get_object(nama_obat)
        pupes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class HamaDetail(APIView):
    """
    Retrieve, update or delete a pupuk pestisida instance
    """
    
    def get_object(self, nama_hama):
        try:
            return Hama.objects.get(nama_hama=nama_hama)
        except Hama.DoesNotExist:
            return Http404
        
    def get(self, request, nama_hama, format=None):
        hama = self.get_object(nama_hama)
        serialzer = HamaSerializer(hama)
        return Response(serialzer.data)
    
    def put(self, request, nama_hama, format=None):
        hama = self.get_object(nama_hama)
        serializer = HamaSerializer(hama, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, nama_hama, format=None):
        hama = self.get_object(nama_hama)
        hama.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TanamanDetail(APIView):
    """
    Retrieve, update or delete a pupuk tanaman instance
    """
    
    def get_object(self, nama_tanaman):
        try:
            return Tanaman.objects.get(nama_tanaman=nama_tanaman)
        except Tanaman.DoesNotExist:
            return Http404
        
    def get(self, request, nama_tanaman, format=None):
        tanaman = self.get_object(nama_tanaman)
        serialzer = TanamanSerializer(tanaman)
        return Response(serialzer.data)
    
    def put(self, request, nama_tanaman, format=None):
        tanaman = self.get_object(nama_tanaman)
        serializer = TanamanSerializer(tanaman, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, nama_tanaman, format=None):
        tanaman = self.get_object(nama_tanaman)
        tanaman.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
