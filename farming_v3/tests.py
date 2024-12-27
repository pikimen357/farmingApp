from django.test import TestCase

# Create your tests here.
from farming_v3.models import Panenan

class PanenanTestCase(TestCase):
    def test_panenan_list(self):
        panenan_list = Panenan.objects.all()
        for panen in panenan_list:
            print(f"Petani: {panen.petaninya.nama}")
            print(f"Tanaman: {panen.hasil_panen.nama_tanaman}")
            print(f"Waktu Tanam: {panen.hasil_panen.waktu_tanam_hari} hari")
            print(f"Berat Panen: {panen.berat_ton} ton\n")
