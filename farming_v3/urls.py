from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from farming_v3 import views

urlpatterns = [
    path('signup/', views.authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    
    path('hama/', views.HamaList.as_view(), name='hama-list'),
    path('hama/<str:nama_hama>/', views.HamaDetailView.as_view(), name="hama-detail"),
    
    path('pestisida-pupuk/', views.PupukPestisidaList.as_view(), name='pestisida-pupuk-list'),
    path('pestisida-pupuk/<str:nama_obat>/', views.PupukPestisidaDetail.as_view(), name='pestisida-pupuk-detail'),
    
    path('tanaman/', views.TanamanList.as_view(), name='tanaman-list'),
    path('tanaman/<str:nama_tanaman>/', views.TanamanDetail.as_view(), name='tanaman-edit'),
    
    path('panenan/<str:hasil_panen__nama_tanaman>/', views.PanenanDetailView.as_view(), name='panenan-detail'),
    path('panenan/', views.PanenanDetailList.as_view(), name='panenan-list'),
    path('panenan-create/', views.PanenanList.as_view(), name='panenan-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)