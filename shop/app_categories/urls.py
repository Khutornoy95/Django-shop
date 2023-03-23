from django.urls import path
from .views import CategoriesView


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='profile'),
    # path('', PasswordView.as_view(), name='password'),
    # path('', AvatarView.as_view(), name='avatar')
]
