from django.urls import path, re_path
from main.views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('', homepage, name='homepage'),
    # path('get/<id>', views.get_single, name='get_single_item'),
    # path('get-todo', views.get_todo, name='get_todo'),
    # path('post-todo', views.save, name='save_data'),
    # path('update-todo', views.update, name='update'),
    # path('token/', views.obtain_auth_token, name='token'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterUser.as_view(), name='register'),

    re_path(r"^todoController/(?P<id>.*)$",TodoView.as_view()),
]