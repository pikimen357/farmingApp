from farming.models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan
from farming.serializers import PetaniSerializer, PanenanSerializer, HamaSerializer, TanamanSerializer, PestisidaPupukSerializer, PanenanDetailSerializer, HamaDetailSerializer
from rest_framework import generics

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class PetaniList(APIView):
#     """
#     List all petani, or create a new petani.
#     """
    
#     def get(self, request, format=None):
#         petani = Petani.objects.all()
#         serializer = PetaniSerializer(petani, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = PetaniSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class PanenanList(APIView):
#     """
#     List all panenan, or create a new panenan.
#     """
    
#     def get(self, request, format=None):
#         panenan = Panenan.objects.all()
#         serializer = PanenanSerializer(panenan, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = PanenanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TanamanList(APIView):
#     """
#     List all tanaman, or create a new tanaman.
#     """
    
#     def get(self, request, format=None):
#         tanaman = Tanaman.objects.all()
#         serializer = TanamanSerializer(tanaman, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = TanamanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class HamaList(APIView):
#     """
#     List all hama, or create a new hama.
#     """
    
#     def get(self, request, format=None):
#         hama = Hama.objects.all()
#         serializer = HamaSerializer(hama, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = HamaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
# class PestisidaPupukList(APIView):
#     """
#     List all pestisida/pupuk, or create a new pestisida/pupuk.
#     """
    
#     def get(self, request, format=None):
#         pupes = PestisidaPupuk.objects.all()
#         serializer = PestisidaPupukSerializer(pupes, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = PestisidaPupukSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

# # DETAIL

# class PetaniDetail(APIView):
#     """
#     Retrieve, update or delete a petani instance
#     """
    
#     # mengambil objek petani
#     def get_object(self, username):
#         try:
#             # mencari petani berdasarkan username
#             return Petani.objects.get(username=username)
        
#         # jika petani tidak ada
#         except Petani.DoesNotExist:
#             return Http404
        
#     def get(self, request, username, format=None):
        
#         # mencari petani berdasarkan username
#         petani = self.get_object(username)
        
#         # menjadikan json dengan serializer objek petani 
#         serialzer = PetaniSerializer(petani)
        
#         # mengembalikan data yang telah di serializer(diubah ke json) berupa response
#         return Response(serialzer.data)
    
#     # membuat objek petani baru
#     def put(self, request, username, format=None):
        
#         # membuat objek petani berdasarkan username
#         petani = self.get_object(username)
        
#         # ubah ke dalam json(srializer) data yang direquest
#         serializer = PetaniSerializer(petani, data=request.data)
        
#         # jika data petani valid maka simpan dan kembalikan response datanya
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         # jika tidak otomatis error 400 bad request
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # menghapus objek petani
#     def delete(self, request, username, format=None):
        
#         # mencari nama
#         petani = self.get_object(username)
        
#         # menghapus petani
#         petani.delete()
        
#         # kembalikan respon 204 
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class PanenanDetail(APIView):
#     """
#     Retrieve, update or delete a panenan instance
#     """
    
#     def get_object(self, pk):
#         try:
#             return Panenan.objects.get(pk=pk)
#         except Panenan.DoesNotExist:
#             return Http404
        
#     def get(self, request, pk, format=None):
#         panenan = self.get_object(pk)
#         serialzer = PanenanSerializer(panenan)
#         return Response(serialzer.data)
    
#     def put(self, request, pk, format=None):
#         panenan = self.get_object(pk)
#         serializer = PanenanSerializer(panenan, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # RIWAYAT PANENAN TIDAK BOLEH DIHAPUS
#     # def delete(self, request, pk, format=None):
#     #     panenan = self.get_object(pk)
#     #     panenan.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
    
# class PupukPestisidaDetail(APIView):
#     """
#     Retrieve, update or delete a pupuk pestisida instance
#     """
    
#     def get_object(self, nama_obat):
#         try:
#             return PestisidaPupuk.objects.get(nama_obat=nama_obat)
#         except PestisidaPupuk.DoesNotExist:
#             return Http404
        
#     def get(self, request, nama_obat, format=None):
#         pupes = self.get_object(nama_obat)
#         serialzer = PestisidaPupuk(pupes)
#         return Response(serialzer.data)
    
#     def put(self, request, nama_obat, format=None):
#         pupes = self.get_object(nama_obat)
#         serializer = PestisidaPupuk(pupes, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, nama_obat, format=None):
#         pupes = self.get_object(nama_obat)
#         pupes.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    

# class HamaDetail(APIView):
#     """
#     Retrieve, update or delete a pupuk pestisida instance
#     """
    
#     def get_object(self, nama_hama):
#         try:
#             return Hama.objects.get(nama_hama=nama_hama)
#         except Hama.DoesNotExist:
#             return Http404
        
#     def get(self, request, nama_hama, format=None):
#         hama = self.get_object(nama_hama)
#         serialzer = HamaSerializer(hama)
#         return Response(serialzer.data)
    
#     def put(self, request, nama_hama, format=None):
#         hama = self.get_object(nama_hama)
#         serializer = HamaSerializer(hama, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, nama_hama, format=None):
#         hama = self.get_object(nama_hama)
#         hama.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class TanamanDetail(APIView):
#     """
#     Retrieve, update or delete a pupuk tanaman instance
#     """
    
#     def get_object(self, nama_tanaman):
#         try:
#             return Tanaman.objects.get(nama_tanaman=nama_tanaman)
#         except Tanaman.DoesNotExist:
#             return Http404
        
#     def get(self, request, nama_tanaman, format=None):
#         tanaman = self.get_object(nama_tanaman)
#         serialzer = TanamanSerializer(tanaman)
#         return Response(serialzer.data)
    
#     def put(self, request, nama_tanaman, format=None):
#         tanaman = self.get_object(nama_tanaman)
#         serializer = TanamanSerializer(tanaman, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, nama_tanaman, format=None):
#         tanaman = self.get_object(nama_tanaman)
#         tanaman.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # menampilkan relasi antara tabel Panenan --> Petani & Tanaman
# class PanenanDetailAPIView(APIView):
#     """
#     API view untuk mendapatkan data detail Panenan.
#     """

#     def get(self, request, *args, **kwargs):
#         panenan = Panenan.objects.all()  # Ambil semua data Panenan
#         serializer = PanenanDetailSerializer(panenan, many=True)  # Serialize data
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class HamaDetailAPIView(APIView):
#     """
#     API view untuk mendapatkan data detail hama.
#     """
    
#     def get(self, request, *args, **kwargs):
#         hama = Hama.objects.all()
#         serializer = HamaDetailSerializer(hama, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# GENERAL OBJECTS

class PetaniList(generics.ListCreateAPIView):
    queryset = Petani.objects.all()
    serializer_class = PetaniSerializer
    
class PanenanList(generics.ListCreateAPIView):
    queryset = Panenan.objects.all()
    serializer_class = PanenanDetailSerializer
    
class TanamanList(generics.ListCreateAPIView):
    queryset = Tanaman.objects.all()
    serializer_class  = TanamanSerializer
    
class HamaList(generics.ListCreateAPIView):
    queryset = Hama.objects.all()
    serializer_class = HamaDetailSerializer
    
class PupukPestisidaList(generics.ListCreateAPIView):
    queryset = PestisidaPupuk.objects.all()
    serializer_class = PestisidaPupukSerializer
    
    
# DETAIL OBJECTS
class PetaniDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetaniSerializer
    
    def get_object(self):
        username = self.kwargs['username']
        return Petani.objects.get(username=username)
    

    
