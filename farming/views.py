from farming.models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan
from farming.serializers import PetaniSerializer, PanenanSerializer, HamaSerializer, TanamanSerializer, PestisidaPupukSerializer, PanenanDetailSerializer, HamaDetailSerializer
from rest_framework import generics

from rest_framework.generics import RetrieveUpdateAPIView

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
    serializer_class = HamaSerializer
    
class PupukPestisidaList(generics.ListCreateAPIView):
    queryset = PestisidaPupuk.objects.all()
    serializer_class = PestisidaPupukSerializer
    
    
# DETAIL OBJECTS
class PetaniDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetaniSerializer
    
    def get_object(self):
        username = self.kwargs['username']
        return Petani.objects.get(username=username)
    

class PanenanDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PanenanDetailSerializer
    lookup_field = 'hasil_panen__nama_tanaman'  # Menggunakan tanaman_nama sebagai path parameter

    def get_queryset(self):
        queryset = Panenan.objects.all()
        #mengambil nama petani dari parameter url 
        petani_nama = self.request.query_params.get('petani_nama') 
        
        if petani_nama is not None:
            # icontains untuk mengambil sebagian petani_nama Vidky -> dky, idk, Vid, dan lain-lain
            queryset = queryset.filter(petaninya__nama__icontains=petani_nama)
            
        return queryset
    
    def get_object(self):
        # Override untuk mendukung lookup melalui relasi
        hasil_panen = self.kwargs.get(self.lookup_field)  # Ambil tanaman_nama dari URL
        return self.get_queryset().get(hasil_panen__nama_tanaman__icontains=hasil_panen)
    
# class PanenanDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PanenanSerializer
    
#     def get_object(self):
#         pass

class PupukPestisidaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PestisidaPupukSerializer
    
    def get_object(self):
        nama_obat = self.kwargs['nama_obat']
        return PestisidaPupuk.objects.get(nama_obat=nama_obat)

class HamaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HamaSerializer
    
    def get_object(self):
        nama_hama = self.kwargs['nama_hama']
        return Hama.objects.get(nama_hama=nama_hama)
    
class TanamanDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TanamanSerializer
    
    def get_object(self):
        nama_tanaman = self.kwargs['nama_tanaman']
        return Tanaman.objects.get(nama_tanaman=nama_tanaman)