from rest_framework import serializers
from farming.models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan

class PetaniSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Petani
        fields = ('id', 'username','password','nama', 'luas_tanah')
        
class PanenanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panenan
        fields = ['id', 'hasil_panen', 'berat_ton']
        
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