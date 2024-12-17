from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from farming import views

urlpatterns = [
    
    path('v1/petani/', views.PetaniList.as_view()),
    path('v1/hama/', views.HamaList.as_view()),
    path('v1/pestisida-pupuk/', views.PupukPestisidaList.as_view()),
    path('v1/tanaman/', views.TanamanList.as_view()),
    path('v1/petani/<str:username>/', views.PetaniDetail.as_view()),
    # path('v1/pestisida-pupuk/<str:nama_obat>/', views.PupukPestisidaDetail.as_view()),
    # path('v1/hama/<str:nama_hama>/', views.HamaDetail.as_view()),
    # path('v1/panenan/<int:pk>/', views.PanenanDetail.as_view()),
    path('v1/panenan/', views.PanenanList.as_view()),
    # path('v1/hama/', views.HamaDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)