from django.urls import path
from farming import views

urlpatterns = [
    path('v1/petani/', views.petani_list),
    path('v1/tanaman/', views.tanaman_list),
    path('v1/panenan/', views.panenan_list),
    path('v1/hama/', views.hama_list),
    path('v1/pupuk-pestisida/', views.pupuk_pestisida_list),
    path('v1/petani/<str:username>/', views.petani_detail),
    path('v1/tanaman/<int:pk>/', views.tanaman_detail),
    path('v1/panenan/<int:pk>/', views.panenan_detail),
]

