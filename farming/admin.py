from django.contrib import admin
from .models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan

# Register your models here.

admin.site.register(Petani)
admin.site.register(Panenan)
admin.site.register(PestisidaPupuk)
admin.site.register(Tanaman)
admin.site.register(Hama)

