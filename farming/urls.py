from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from farming import views

urlpatterns = [
    # path('v1/petani/', views.petani_list),
    # path('v1/tanaman/', views.tanaman_list),
    # path('v1/panenan/', views.panenan_list),
    # path('v1/hama/', views.hama_list),
    # path('v1/pupuk-pestisida/', views.pupuk_pestisida_list),
    path('v1/petani/', views.PetaniList.as_view()),
    path('v1/panenan/', views.PanenanList.as_view()),
    path('v1/hama/', views.HamaList.as_view()),
    path('v1/pestisida-pupuk/', views.PestisidaPupukList.as_view()),
    path('v1/tanaman/', views.TanamanList.as_view()),
    path('v1/petani/<str:username>/', views.PetaniDetail.as_view()),
    path('v1/pestisida-pupuk/<str:nama_obat>/', views.PupukPestisidaDetail.as_view()),
    path('v1/hama/<str:nama_hama>/', views.HamaDetail.as_view()),
    path('v1/panenan/<int:pk>/', views.PanenanDetail.as_view()),
    # path('v1/tanaman/<int:pk>/', views.tanaman_detail),
    # path('v1/panenan/<int:pk>/', views.panenan_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)