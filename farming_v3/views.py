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
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login berhasil")
            return redirect("http://localhost:8000/v3/tanaman")  # Ganti dengan halaman tujuan setelah login
        else:
            messages.error(request, "Username atau password salah")
    
    return render(request, "login.html")

# GENERAL OBJECTS
    
class UserList(StaffEditorPermissionMixin, 
               generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#  user cannot add panenan here
class PanenanDetailList(StaffEditorPermissionMixin, 
                        UserQuerySetMixin, 
                        generics.ListAPIView):
    queryset = Panenan.objects.all()
    serializer_class = PanenanDetailSerializer
   

# user can add panenan here
class PanenanList(  
                    StaffEditorPermissionMixin,
                    UserQuerySetMixin,
                    generics.ListCreateAPIView
                ):
    queryset = Panenan.objects.all()
    serializer_class = PanenanSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    
    def perform_create(self, serializer):
        hasil_panen = serializer.validated_data.get('hasil_panen')
        owner = self.request.user
        berat_ton = serializer.validated_data.get('berat_ton', 0)
        created = serializer.validated_data.get('created')
        
        # jika belum ada panenan dengan nama dan petani sama --> create
        # jika sudah ada panenan dengan nama dan petani sama --> update
        panen_obj, createdd = Panenan.objects.get_or_create(
            hasil_panen=hasil_panen,
            owner=owner,
            defaults={
                'berat_ton' : berat_ton,
                'created' : created,
            }
        )
        
        if not createdd:
            # Jika data sudah ada, tambahkan jumlah ton dan perbarui tanggal panen
            panen_obj.berat_ton += berat_ton
            panen_obj.created = created
            panen_obj.save(update_fields=['berat_ton', 'created'])
        
        # else:
        #     serializer.save(owner=self.request.user)
    
class TanamanList (
                  StaffEditorPermissionMixin, 
                  UserQuerySetMixin, 
                  generics.ListCreateAPIView
                  ):
    queryset = Tanaman.objects.all()
    serializer_class  = TanamanSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class HamaList(StaffEditorPermissionMixin,
            #    UserQuerySetMixin,
               generics.ListCreateAPIView):
    queryset = Hama.objects.all()
    serializer_class = HamaSerializer
    
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
        queryset = Panenan.objects.all()
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
    serializer_class = HamaSerializer
    
    # mengambil data hama berdasarkan namanya
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