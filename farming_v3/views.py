from farming_v3.models import  PestisidaPupuk, Tanaman, Hama, Panenan
from farming_v3.serializers import  PanenanSerializer, HamaSerializer, TanamanSerializer, PestisidaPupukSerializer, PanenanDetailSerializer, HamaDetailSerializer
from rest_framework import generics, mixins, permissions
from django.contrib.auth.models import User
from farming_v3.serializers import UserSerializer
from rest_framework.response  import Response
from farming_v3.permissions import IsOwnerOrReadOnly
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Cache
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

# Redis Test
def factorial_with_cache(request, n):
    n = int(n)
    result = cache.get(f'factorial_{n}')

    if result is None:
        result = 1
        for i in range(1, n + 1):
            result *= i
        cache.set(f'factorial_{n}', result, 60)  # Cache for 60 seconds

    return HttpResponse(f'Factorial of {n} is: {result}')

# GENERAL OBJECTS
    
class UserList(StaffEditorPermissionMixin, 
               generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#  user cannot add panenan here
class PanenanDetailList(StaffEditorPermissionMixin, 
                        UserQuerySetMixin, 
                        generics.ListAPIView):
    queryset = Panenan.objects.all().select_related('owner', 'hasil_panen')
    serializer_class = PanenanDetailSerializer
   

# user can add panenan here
class PanenanList(  
                    StaffEditorPermissionMixin,
                    UserQuerySetMixin,
                    generics.ListCreateAPIView
                ):
    queryset = Panenan.objects.all().select_related('owner', 'hasil_panen')
    serializer_class = PanenanSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    # def perform_create(self, serializer):
    #     hasil_panen = serializer.validated_data.get('hasil_panen')
    #     owner = self.request.user
    #     berat_ton = serializer.validated_data.get('berat_ton', 0)
    #     created = serializer.validated_data.get('created')
        
    #     # jika belum ada panenan dengan nama dan petani sama --> create
    #     # jika sudah ada panenan dengan nama dan petani sama --> update
    #     panen_obj, createdd = Panenan.objects.get_or_create(
    #         hasil_panen=hasil_panen,
    #         owner=owner,
    #         defaults={
    #             'berat_ton' : berat_ton,
    #             'created' : created,
    #         }
    #     )
        
    #     if not createdd:
    #         # Jika data sudah ada, tambahkan jumlah ton dan perbarui tanggal panen
    #         panen_obj.berat_ton += berat_ton
    #         panen_obj.created = created
    #         panen_obj.save(update_fields=['berat_ton', 'created'])
        
        # else:
        #     serializer.save(owner=self.request.user)
    
# @method_decorator(cache_page(60 * 15), name="dispatch")
class TanamanList (
                  StaffEditorPermissionMixin, 
                  UserQuerySetMixin, 
                  generics.ListCreateAPIView
                  ):
    queryset = Tanaman.objects.all().select_related('owner', 'peluang_hama')
    serializer_class  = TanamanSerializer
    
    # caching
    @method_decorator(cache_page(60*15, key_prefix="tanaman_list")) 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    # caching
    def get_queryset(self):
        import time
        time.sleep(3)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class HamaList(StaffEditorPermissionMixin,
            #    UserQuerySetMixin,
               generics.ListCreateAPIView):
    queryset = Hama.objects.all().select_related('obat')
    serializer_class = HamaSerializer
    
    @method_decorator(cache_page(60*15, key_prefix="hama_list")) 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    # caching
    def get_queryset(self):
        import time
        time.sleep(3)
        return super().get_queryset()
    
class PupukPestisidaList(StaffEditorPermissionMixin, 
                        #  UserQuerySetMixin,
                         generics.ListCreateAPIView):
    queryset = PestisidaPupuk.objects.all()
    serializer_class = PestisidaPupukSerializer

class UserDetail(StaffEditorPermissionMixin, 
                 generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# can't update panenan, when panenan already exist with same farmer  (must be updated)
class PanenanDetailView(StaffEditorPermissionMixin, 
                        UserQuerySetMixin, 
                        generics.RetrieveAPIView):
    serializer_class = PanenanDetailSerializer
    lookup_field = 'hasil_panen__nama_tanaman'  # Menggunakan tanaman_nama sebagai path parameter
    
    
    def get_queryset(self):
        queryset = Panenan.objects.all().select_related('owner', 'hasil_panen')
        #mengambil nama petani dari parameter url 
        petani_nama = self.request.query_params.get('petani_nama') 
        
        if petani_nama:
            # icontains untuk mengambil sebagian petani_nama Vidky -> dky, idk, Vid, dan lain-lain
            queryset = queryset.filter(owner__username__icontains=petani_nama)
            
        return queryset
    
    def get_object(self):
        # Override untuk mendukung lookup melalui relasi
        hasil_panen = self.kwargs.get(self.lookup_field)  # Ambil tanaman_nama dari URL
        return self.get_queryset().get(hasil_panen__nama_tanaman__icontains=hasil_panen)

class PupukPestisidaDetail(StaffEditorPermissionMixin, 
                            # UserQuerySetMixin, 
                            generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PestisidaPupukSerializer
    
    def get_object(self):
        nama_obat = self.kwargs['nama_obat']
        return PestisidaPupuk.objects.get(nama_obat=nama_obat)

class HamaDetailView( StaffEditorPermissionMixin, 
                        # UserQuerySetMixin, 
                        generics.RetrieveUpdateDestroyAPIView):
    # serializer_class = HamaSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HamaDetailSerializer  # Serializer specially for  GET
        return HamaSerializer  #Default  serializer for PUT, PATCH, and DELETE
    
    # get object hama by it's name  
    def get_object(self):
        nama_hama = self.kwargs['nama_hama']
        return Hama.objects.get(nama_hama=nama_hama)
    
class TanamanDetail(StaffEditorPermissionMixin, 
                    UserQuerySetMixin, 
                    generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TanamanSerializer
    
    
    def get_object(self):
        nama_tanaman = self.kwargs['nama_tanaman']
        return Tanaman.objects.get(nama_tanaman=nama_tanaman)
    
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})