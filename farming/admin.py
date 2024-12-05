from django.contrib import admin
from .models import Petani, Panenan, Tanaman, PestisidaPupuk, Hama

# Register your models here.

admin.site.register(Petani)
admin.site.register(Panenan)
admin.site.register(Tanaman)
admin.site.register(PestisidaPupuk)
admin.site.register(Hama)

