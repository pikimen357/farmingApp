from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tanaman, Hama, PestisidaPupuk

User = get_user_model()

class TanamanListTestCase(APITestCase):
    def setUp(self):
        # Menghapus semua data sebelum test
        Tanaman.objects.all().delete()
        Hama.objects.all().delete()
        PestisidaPupuk.objects.all().delete()
        
        # Membuat user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Membuat instance PestisidaPupuk (obat untuk hama)
        self.obat = PestisidaPupuk.objects.create(nama='Fungisida X')
        
        # Membuat instance Hama
        self.hama = Hama.objects.create(
            nama_hama='cendawan',
            rate_bahaya=3,
            makhluk='TUMBUHAN',
            obat=self.obat,
            deskripsi='Deskripsi Hama'
        )
        
        # Menyiapkan data tanaman
        self.tanaman_data = {
            'nama_tanaman': 'jeruk',
            'jenis': 'pohon',
            'waktu_tanam_hari': 419,
            'harga_perTon': 2000000000,
            'peluang_hama': self.hama.id,
            'public': True
        }
        
    def test_create_tanaman(self):
        response = self.client.post('/v3/tanaman/', self.tanaman_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tanaman.objects.count(), 1)
        self.assertEqual(Tanaman.objects.first().nama_tanaman, 'jeruk')
        
    def test_list_tanaman(self):
        # Pastikan database bersih sebelum test
        Tanaman.objects.all().delete()
        
        # Buat satu tanaman saja
        Tanaman.objects.create(
            nama_tanaman='jeruk',
            jenis='pohon',
            waktu_tanam_hari=419,
            harga_perTon=2000000000,
            peluang_hama=self.hama,
            public=True,
            owner=self.user
        )
        
        response = self.client.get('/v3/tanaman/')
        print("Response Data:", response.data)  # Debugging
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Pastikan hanya 1 data yang diterima
        self.assertEqual(response.data['results'][0], 'jeruk')
