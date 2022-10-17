from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView


# /api/
urlpatterns = [
    path('products', views.ProductListCreateAPIView.as_view()),
    path('products/<str:article>', views.ProductRetrieveUpdateDestroyAPIView.as_view()),

    path('users', views.UserListCreateAPIView.as_view()),
    path('users/<str:username>', views.UserRetrieveUpdateDestroyAPIView.as_view()),

    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]