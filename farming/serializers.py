from rest_framework import serializers
from farming.models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan

class PetaniSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Petani
        fields = ('id', 'username','password','nama', 'luas_tanah')
        
class PanenanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panenan
        fields = ['id', 'hasil_panen','petaninya', 'berat_ton']
        
class TanamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanaman
        fields = ['id', 'nama_tanaman', 'jenis', 'waktu_tanam_hari']

class PestisidaPupukSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestisidaPupuk
        fields = ['id', 'jenis', 'nama_obat', 'produsen', 'warna']
        
class HamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hama
        fields = ['id', 'nama_hama', 'rate_bahaya', 'makhluk', 'obat']
        
class PanenanDetailSerializer(serializers.ModelSerializer):
    petani_nama = serializers.CharField(source='petaninya.nama', read_only=True)
    # tanaman_nama = serializers.CharField(source='hasil_panen.nama_tanaman', read_only=True)
    tanaman_nama = serializers.CharField(source='hasil_panen.nama_tanaman', read_only=True)
    waktu_tanam = serializers.IntegerField(source='hasil_panen.waktu_tanam_hari', read_only=True)
    tanggal_panen = serializers.DateTimeField(source='created')
    harga = serializers.IntegerField(source='hasil_panen.harga_perTon', read_only=True)
    total_harga = serializers.SerializerMethodField()

    class Meta:
        model = Panenan
        fields = ['id','tanggal_panen', 'petani_nama', 'tanaman_nama', 'waktu_tanam', 'berat_ton','harga', 'total_harga']
        
    def get_total_harga(self, obj):
        # Menghitung total pendapatan
        return obj.berat_ton * obj.hasil_panen.harga_perTon
        
class HamaDetailSerializer(serializers.ModelSerializer):
    nama_hama = serializers.CharField( read_only=True)
    
    # source hanya untuk mengambil data dari tabel relasi (relasi ke pestisida pupuk)
    # bukan tabel nys sendiri (hama)
    nama_obat = serializers.CharField(source='obat.nama_obat', read_only=True)
    makhluk = serializers.CharField(read_only=True)
    
    class Meta:
        model = Hama
        fields = ['id', 'nama_hama', 'nama_obat', 'makhluk']