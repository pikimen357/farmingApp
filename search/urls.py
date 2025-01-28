from django .urls import path

from . import views

urlpatterns = [
    path('', views.SearchTanmanListView.as_view(), name='search')
]
