from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL # 'auth.User'

class PestisidaPupuk(models.Model):
    class Warna(models.TextChoices):
        HITAM = "HITAM"
        PUTIH = "PUTIH"
        MERAH = "MERAH"
        KUNING = "KUNING"

    class Jenis(models.TextChoices):
        PESTISIDA = "PESTISIDA"
        PUPUK = "PUPUK"
    
    created = models.DateTimeField(auto_now_add=True)
    jenis = models.TextField(max_length=10, choices=Jenis.choices)
    nama_obat = models.CharField(max_length=100, unique=True)
    produsen = models.CharField(max_length=100)
    warna = models.TextField(max_length=10, choices=Warna.choices)
   
    class Meta:
        ordering = ['created']
        db_table = 'pestisida_pupuk'    
        
    def __str__(self):
        return f"{self.nama_obat} diproduksi {self.produsen}, warna {self.warna}"
     
class Hama(models.Model):
    class Makhluk(models.TextChoices):
        TUMBUHAN = "TUMBUHAN"
        HEWAN = "HEWAN"
    
    created = models.DateTimeField(auto_now_add=True)
    nama_hama = models.CharField(max_length=100, unique=True)
    rate_bahaya = models.IntegerField(default=0)
    obat = models.ForeignKey(PestisidaPupuk, on_delete=models.RESTRICT)
    makhluk =models.CharField(max_length=20, choices=Makhluk.choices)
    
    class Meta:
        ordering = ['-rate_bahaya']
        db_table = 'hama'
    
    def __str__(self):
        return self.nama_hama
    
    
    
# for searching Tanaman

class TanamanQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(nama_tanaman__icontains=query)
        qs = self.is_public().filter(lookup)
        
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        
        return qs

class TanamanManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TanamanQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().is_public().search(query, user=user)


# searching Tanaman
class Tanaman(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nama_tanaman = models.CharField(max_length=100, unique=True)
    jenis = models.CharField(max_length=100)
    waktu_tanam_hari = models.IntegerField(default=0)
    harga_perTon = models.IntegerField(default=0)
    peluang_hama = models.ForeignKey(Hama, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='tanaman', on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    
    objects = TanamanManager() # can't migerate
    
    class Meta:
        ordering = ['-harga_perTon']
        db_table = 'tanaman'
    
    def __str__(self):
        return self.nama_tanaman
    
    
class Panenan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    # foreign key merujuk pada id tabel Tanaman
    hasil_panen = models.ForeignKey(Tanaman, on_delete=models.RESTRICT)
    berat_ton = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='panenan', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.hasil_panen.nama_tanaman} - {self.berat_ton} ton"
    
    class Meta:
        ordering = ['created']
        db_table = 'panenan'

