from django.urls import path
from features.api.views import CategoryListAV, UserListAV, UpdateAV, UserDetailAV, TransactionAV, Login, ParkingAV, CategoryDataDetails, TransactionUser, ParkingExitAV

urlpatterns = [
    path('category/', CategoryListAV.as_view(), name='all-category-list'),
    path('user/<int:pk>/', UserDetailAV.as_view(), name='user-detail'),
    path('user/', UserListAV.as_view(), name='user-list'),
    path('transaction/<int:pk>/', TransactionUser.as_view(), name='transaction'),
    path('login/', Login.as_view(), name='login'),
    path('parking/', ParkingAV.as_view(), name='parking'),
    path('category/<int:pk>/', CategoryDataDetails.as_view(), name='category-details'),
    path('transactions/',ParkingExitAV.as_view(), name='transaction-details'),
    path('update/<int:pk>/', UpdateAV.as_view(), name='cat-update-details'),
    ]