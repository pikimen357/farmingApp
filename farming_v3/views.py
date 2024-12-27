from farming_v3.models import  PestisidaPupuk, Tanaman, Hama, Panenan
from farming_v3.serializers import  PanenanSerializer, HamaSerializer, TanamanSerializer, PestisidaPupukSerializer, PanenanDetailSerializer, HamaDetailSerializer
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth.models import User
from farming_v3.serializers import UserSerializer
from rest_framework import permissions
from farming_v3.permissions import IsOwnerOrReadOnly

# GENERAL OBJECTS
# class PetaniList(generics.ListCreateAPIView):
#     queryset = Petani.objects.all()
#     serializer_class = PetaniSerializer
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PanenanDetailList(generics.ListCreateAPIView):
    queryset = Panenan.objects.all()
    serializer_class = PanenanDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class PanenanList(generics.ListCreateAPIView):
    queryset = Panenan.objects.all()
    serializer_class = PanenanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class TanamanList(generics.ListCreateAPIView):
    queryset = Tanaman.objects.all()
    serializer_class  = TanamanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class HamaList(generics.ListCreateAPIView):
    queryset = Hama.objects.all()
    serializer_class = HamaSerializer
    
class PupukPestisidaList(generics.ListCreateAPIView):
    queryset = PestisidaPupuk.objects.all()
    serializer_class = PestisidaPupukSerializer
    
    
# DETAIL OBJECTS
# class PetaniDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PetaniSerializer
    
#     def get_object(self):
#         username = self.kwargs['username']
#         return Petani.objects.get(username=username)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PanenanDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PanenanDetailSerializer
    lookup_field = 'hasil_panen__nama_tanaman'  # Menggunakan tanaman_nama sebagai path parameter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        queryset = Panenan.objects.all()
        return queryset
    
    # def get_queryset(self):
    #     queryset = Panenan.objects.all()
    #     #mengambil nama petani dari parameter url 
    #     petani_nama = self.request.query_params.get('petani_nama') 
        
    #     if petani_nama:
    #         # icontains untuk mengambil sebagian petani_nama Vidky -> dky, idk, Vid, dan lain-lain
    #         queryset = queryset.filter(petaninya__nama__icontains=petani_nama)
            
    #     return queryset
    
    def get_object(self):
        # Override untuk mendukung lookup melalui relasi
        hasil_panen = self.kwargs.get(self.lookup_field)  # Ambil tanaman_nama dari URL
        return self.get_queryset().get(hasil_panen__nama_tanaman__icontains=hasil_panen)

class PupukPestisidaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PestisidaPupukSerializer
    
    def get_object(self):
        nama_obat = self.kwargs['nama_obat']
        return PestisidaPupuk.objects.get(nama_obat=nama_obat)

class HamaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HamaSerializer
    
    # mengambil data hama berdasarkan namanya
    def get_object(self):
        nama_hama = self.kwargs['nama_hama']
        return Hama.objects.get(nama_hama=nama_hama)
    
class TanamanDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TanamanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_object(self):
        nama_tanaman = self.kwargs['nama_tanaman']
        return Tanaman.objects.get(nama_tanaman=nama_tanaman)