from django.urls import path
from .views import BoxCreateView, BoxUpdateView, BoxListView, MyBoxListView, BoxDeleteView

urlpatterns = [
    path('boxes/', BoxListView.as_view(), name='box-list'),
    path('boxes/my/', MyBoxListView.as_view(), name='my-box-list'),
    path('boxes/add/', BoxCreateView.as_view(), name='box-add'),
    path('boxes/<int:pk>/update/', BoxUpdateView.as_view(), name='box-update'),
    path('boxes/<int:pk>/delete/', BoxDeleteView.as_view(), name='box-delete'),
]
