from rest_framework import serializers
from farming_v3.models import  PestisidaPupuk, Tanaman, Hama, Panenan
from django.contrib.auth.models import User
from api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse
from django.utils.timezone import now

        
class PanenanSerializer(serializers.ModelSerializer):
    tanggal_panen = serializers.DateTimeField(source='created',  format='%Y-%m-%d %H:%M:%S')
    owner = serializers.ReadOnlyField(source='user', read_only=True)
    deskripsi = serializers.SerializerMethodField()
    class Meta:
        model = Panenan
        
        fields = ['id', 'hasil_panen', 'berat_ton', 'tanggal_panen', 'deskripsi', 'owner']
    
    def get_deskripsi(self, obj):
        return f"Panenan {obj.hasil_panen.nama_tanaman} dengan berat {obj.berat_ton}"
        
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    
    def validate_berat_ton(self, value):
        if value <= 0:
            raise serializers.ValidationError("berat harus lebih dari 0")
        return value
    
    def validate_tanggal_panen(self, value):
        if value > now():
            raise serializers.ValidationError("Tidak boleh melebihi tanggal hari ini")
        return value
        
class TanamanSerializer(serializers.ModelSerializer):
    
    class TanamanInlineSerializer(serializers.Serializer):
        url = serializers.HyperlinkedIdentityField(
                view_name = 'tanaman-edit',
                lookup_field = 'nama_tanaman',
                read_only=True
        )
        
        nama_tanaman = serializers.CharField(read_only=True)
    

    edit_url = serializers.SerializerMethodField(read_only=True)
    # related_tanaman = TanamanInlineSerializer(source='owner.tanaman.all', read_only=True, many=True) 
    owner = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Tanaman
        fields = [
                    'edit_url', 
                    'owner',
                    'id', 
                    'nama_tanaman', 
                    'jenis', 
                    'waktu_tanam_hari', 
                    'harga_perTon', 
                    'peluang_hama', 
                    'link_tanaman',
                    'public',
                    'deskripsi',
                    # 'related_tanaman'
                ]

    def get_edit_url(self, obj):
        request = self.context.get('request')
        
        if request is None:
            return None
        
        
        return reverse('tanaman-edit', kwargs={'nama_tanaman' : obj.nama_tanaman}, request=request)
    
    def to_internal_value(self, data):
        
        # ensure certain fields are converted to integer
        data["owner"] = int(data["owner"]) if "owner" in data else None
        data["waktu_tanam_hari"] = int(data["waktu_tanam_hari"]) if "waktu_tanam_hari" in data else None
        data["harga_perTon"] = int(data["harga_perTon"]) if "harga_perTon" in data else None
        data["peluang_hama"] = int(data["peluang_hama"]) if "peluang_hama" in data else None
        
        return super().to_internal_value(data)
    
    def validate_waktu_tanam_hari(self, value): 
        if value <= 0:
            raise serializers.ValidationError("waktu tanam harus lebih dari 0")
        return value
    
    def validate_harga_perTon(self, value): 
        if value <= 0:
            raise serializers.ValidationError("harga harus lebih dari 0")
        return value
    
class PestisidaPupukSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestisidaPupuk
        fields = ['id', 'jenis', 'nama_obat', 'produsen', 'warna', 'deskripsi']
        
class HamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hama
        fields = ['id', 'nama_hama', 'rate_bahaya', 'makhluk', 'obat', 'deskripsi']
        
    def validate_rate_bahaya(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("rate harus 1 - 5")
        return value

# Serializer for table relation panenan --> tanaman, panenan --> petani 
class PanenanDetailSerializer(serializers.ModelSerializer):
    tanaman_nama = serializers.CharField(source='hasil_panen.nama_tanaman', read_only=True)
    waktu_tanam = serializers.IntegerField(source='hasil_panen.waktu_tanam_hari', read_only=True)
    
    # if the column name diffrent ro serializer name, use source
    tanggal_panen = serializers.DateTimeField(source='created',  format='%Y-%m-%d %H:%M:%S', read_only=True)
    harga = serializers.IntegerField(source='hasil_panen.harga_perTon', read_only=True)
    total_harga = serializers.SerializerMethodField(read_only=True)
    petani = serializers.ReadOnlyField(source='owner.username', read_only=True)
    deskripsi = serializers.SerializerMethodField(read_only=True)
    
    # edit_url = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = Panenan
        fields = [
            
            'id',
            'tanggal_panen', 
            'tanaman_nama', 
            'waktu_tanam', 
            'berat_ton',
            'harga', 
            'total_harga',
            'petani', 
            'deskripsi',
            # 'edit_url'
            
            ]
        
    def get_total_harga(self, obj):
        # Menghitung total pendapatan
        return obj.berat_ton * obj.hasil_panen.harga_perTon

    def get_deskripsi(self,obj):
        if obj.berat_ton > 100:
            return f"Panenan {obj.hasil_panen.nama_tanaman} dengan hasil yang melimpah"
        return f"Panenan {obj.hasil_panen.nama_tanaman} dengan berat {obj.berat_ton}"
    
# Serializer for table relation panenan -->- tanaman
class HamaDetailSerializer(serializers.ModelSerializer):
    nama_hama = serializers.CharField( read_only=True)
    
    # source hanya untuk mengambil data dari tabel relasi (relasi ke pestisida pupuk)
    # bukan tabel nys sendiri (hama)
    nama_obat = serializers.CharField(source='obat.nama_obat', read_only=True)
    makhluk = serializers.CharField(read_only=True)
    rate_bahaya = serializers.CharField(read_only=True)
    
    class Meta:
        model = Hama
        fields = ['id', 'nama_hama', 'nama_obat', 'makhluk', 'rate_bahaya']
    
    def validate_rate_bahaya(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("rate harus 1 - 5")
        return value
        
        
class UserSerializer(serializers.ModelSerializer):
    
    # untuk timbal balik antara relasi, karena jika  tanaman --> user tidak secara otomatis tanaman --> user 
    panenan = serializers.PrimaryKeyRelatedField(many=True, queryset=Panenan.objects.all())
    tanaman = serializers.PrimaryKeyRelatedField(many=True, queryset=Tanaman.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'panenan', 'tanaman']