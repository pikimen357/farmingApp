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
    


class PanenanDetail(RetrieveUpdateAPIView):
    serializer_class = PanenanDetailSerializer
    lookup_field = 'hasil_panen'  # Menggunakan tanaman_nama sebagai path parameter

    def get_queryset(self):
        queryset = Panenan.objects.all()
        #mengambil nama petani dari parameter url 
        petani_nama = self.request.query_params.get('petani_nama') 
        
        if petani_nama is not None:
            queryset = queryset.filter(petaninya__nama=petani_nama)
            
        return queryset
    
    def get_object(self):
        # Override untuk mendukung lookup melalui relasi
        hasil_panen = self.kwargs.get(self.lookup_field)  # Ambil tanaman_nama dari URL
        return self.get_queryset().get(hasil_panen=hasil_panen)

    
    
