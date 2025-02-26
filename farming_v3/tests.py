from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tanaman, Hama, PestisidaPupuk, Panenan



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
        self.obat = PestisidaPupuk.objects.create(
            jenis="PESTISIDA",
            nama_obat="Joilling",
            produsen="farmacolor",
            warna="PUTIH",
            deskripsi="joiling is very impactfull for dangerous hama"
        )
        
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
            'nama_tanaman': 'jahe',
            'jenis': 'ubian',
            'waktu_tanam_hari': 419,
            'harga_perTon': 100000000000,
            'peluang_hama': self.hama.id,
            'public': True
        }
        
    def test_create_tanaman(self):
        response = self.client.post('/v3/tanaman/', self.tanaman_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PestisidaPupuk.objects.count(), 1)
        self.assertEqual(Hama.objects.count(), 1)
        self.assertEqual(Tanaman.objects.count(), 1)
        self.assertEqual(Tanaman.objects.first().nama_tanaman, 'jahe')
        
    def test_list_tanaman(self):
        # Pastikan database bersih sebelum test
        Tanaman.objects.all().delete()
        
        
        
        # # Buat satu tanaman saja
        Tanaman.objects.create(
            nama_tanaman='jahe',
            jenis='ubian',
            waktu_tanam_hari=419,
            harga_perTon=100000000000,
            peluang_hama=self.hama,
            public=True,
            owner=self.user
        )
        
       
        response = self.client.get('/v3/tanaman/')
       
        print("Response Data:", response.data)  # Debugging
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Pastikan hanya 1 data yang diterima
        self.assertEqual(response.data['results'][0]['nama_tanaman'], 'jahe')
        self.assertEqual(response.data['results'][0]['harga_perTon'], 100000000000)
        
        
class PanenanCreateTestCase(APITestCase):
    def setUp(self):
        Tanaman.objects.all().delete()
        Panenan.objects.all().delete()
        Hama.objects.all().delete()
        PestisidaPupuk.objects.all().delete()
        
        self.user = User.objects.create(username='hendrik', password='hendrikjahat')
        self.client.login(username='hendrik', password='hendrikjahat')
        
        self.obat = PestisidaPupuk.objects.create(
            jenis="PESTISIDA",
            nama_obat="Joilling",
            produsen="farmacolor",
            warna="PUTIH",
            deskripsi="joiling is very impactfull for dangerous hama"
        )
        
        # Membuat instance Hama
        self.hama = Hama.objects.create(
            nama_hama='cendawan',
            rate_bahaya=3,
            makhluk='TUMBUHAN',
            obat=self.obat,
            deskripsi='Deskripsi Hama'
        )
        
        self.tanaman = Tanaman.objects.create(

            nama_tanaman="beras merah",
            jenis="legum",
            waktu_tanam_hari=75,
            harga_perTon=7000000,
            peluang_hama=self.hama,
            deskripsi="deskripsi tanaman",
            link_tanaman="https://trans89.com/media/upload/2022/10/Tangerang-Dorong-Pasar-Besar-Sektor-Pertanian-Dengan-Budidaya-Tanaman-Pangan-Organik-653x366.jpg",
            public=True,
            owner=self.user
        )
        

        self.panenan_data = {
            "hasil_panen": self.tanaman.id,
            "berat_ton": 415,
            "tanggal_panen": "2025-01-28 11:32:48",
            "deskripsi": "Deskripsi Panenan"
        }

    def test_create_panenan(self):
        response = self.client.post('/v3/panenan-create/', self.panenan_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Panenan.objects.count(), 1)
        self.assertEqual(Panenan.objects.first().hasil_panen, self.tanaman.id)
        self.assertEqual(Panenan.objects.first().berat_ton, 415)
        





            
            