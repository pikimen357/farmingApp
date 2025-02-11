from django .urls import path

from . import views

urlpatterns = [
    path('tanaman/', views.SearchTanmanListView.as_view(), name='tanaman-search')
]
