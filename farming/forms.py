from django import forms
from .models import Petani

class PetaniForm(forms.ModelForm):
    class Meta:
        model = Petani
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        nama = cleaned_data.get('nama')

        if Petani.objects.filter(username=username, nama=nama).exists():
            raise forms.ValidationError(f"Petani dengan username '{username}' dan nama '{nama}' sudah ada.")
        
        return cleaned_data
