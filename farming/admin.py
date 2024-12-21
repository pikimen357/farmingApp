from django.contrib import admin
from .models import Petani, PestisidaPupuk, Tanaman, Hama, Panenan
from .forms import PetaniForm

# Register your models here.

@admin.register(Petani)
class PetaniAdmin(admin.ModelAdmin):
    form = PetaniForm

# admin.site.register(Petani)
admin.site.register(Panenan)
admin.site.register(PestisidaPupuk)
admin.site.register(Tanaman)
admin.site.register(Hama)

