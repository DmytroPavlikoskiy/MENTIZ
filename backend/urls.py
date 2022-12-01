from django.urls import path
from .views import home
# from .views import UserProfileListView, UserProfileDetailView, UserCreate
from rest_framework_simplejwt.views import TokenRefreshView
# from register.views import MyObtainTokenPairView, RegisterView

app_name = 'back'
urlpatterns = [
    path('', home, name='home'),
    # path('register/', UserCreate.as_view(), name="register"),
    # path('all-profiles/', TokenRefreshView.as_view(), name="all-profiles"),
    # path('profile/<int:pk>/', RegisterView.as_view(), name="profile"),
]