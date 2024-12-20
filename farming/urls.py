from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from farming import views

urlpatterns = [
    
    path('petani/', views.PetaniList.as_view()),
    path('hama/', views.HamaList.as_view()),
    path('hama/<str:nama_hama>/', views.HamaDetailView.as_view(), name=""),
    path('pestisida-pupuk/', views.PupukPestisidaList.as_view()),
    path('tanaman/', views.TanamanList.as_view()),
    path('petani-detail/<str:username>/', views.PetaniDetail.as_view()),
    path('pestisida-pupuk/<str:nama_obat>/', views.PupukPestisidaDetail.as_view()),
    # path('hama/<str:nama_hama>/', views.HamaDetail.as_view()),
    
    path('panenan/<str:hasil_panen__nama_tanaman>/', views.PanenanDetailView.as_view(), name='panenan-detail'),
    path('panenan/', views.PanenanList.as_view()),
    # path('hama/', views.HamaDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)