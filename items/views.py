from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .permissions import IsAuthenticatedOrSafeMethods

from .models import Category, Item, User
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication ]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


@api_view(http_method_names=['GET', ])
@authentication_classes([BasicAuthentication, ])
# @permission_classes([IsAuthenticated, ])
def get_user_info(request):
    user = request.user
    data = {
        'username': user.username,
        'password': user.password
    }
    return Response(data)


@api_view(http_method_names=['POST'])
def user_register(request):
    serializers = UserRegisterSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors, status=400)