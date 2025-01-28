from rest_framework import generics 

from farming_v3.models import  Tanaman
from farming_v3.serializers import TanamanSerializer

class SearchTanmanListView(generics.ListAPIView):
    queryset = Tanaman.objects.all()
    serializer_class = TanamanSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Tanaman.objects.none()
        
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)           
            
        return results