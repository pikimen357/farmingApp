from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from farming_v3 import views

urlpatterns = [
    
    
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    
    path('hama/', views.HamaList.as_view()),
    path('hama/<str:nama_hama>/', views.HamaDetailView.as_view(), name=""),
    
    path('pestisida-pupuk/', views.PupukPestisidaList.as_view()),
    path('pestisida-pupuk/<str:nama_obat>/', views.PupukPestisidaDetail.as_view()),
    
    path('tanaman/', views.TanamanList.as_view()),
    path('tanaman/<str:nama_tanaman>/', views.TanamanDetail.as_view()),
    
    path('panenan/<str:hasil_panen__nama_tanaman>/', views.PanenanDetailView.as_view(), name='panenan-detail'),
    path('panenan/', views.PanenanDetailList.as_view()),
    path('panenan-list/', views.PanenanList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)