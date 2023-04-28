from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
# from rest_framework.views import

from . import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('item', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_info/', views.get_user_info),
    path('register/', views.user_register),
    path('auth_token/', auth_views.obtain_auth_token),
    path('auth/', include('rest_framework.urls')),

]
#каких случаях нужно ставить ()
    #
    # path('category/', views.CategoryViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('items/', views.ItemViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # ))
