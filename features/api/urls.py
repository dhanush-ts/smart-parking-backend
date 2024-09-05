from django.urls import path
from features.api.views import CategoryListAV, UserListAV, UserDetailAV

urlpatterns = [
    path('category/', CategoryListAV.as_view(), name='all-category-list'),
    path('user/<int:pk>/', UserDetailAV.as_view(), name='user-detail'),
    path('user/', UserListAV.as_view(), name='user-list'),
    ]