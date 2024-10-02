from rest_framework import viewsets
from .models import AppUser,Manufacturer,Picture,Stock,Temperature,WebUser
from .serializers import AppUserSerializer,ManufacturerSerializer,PictureSerializer,StockSerializer,TemperatureSerializer,WebUserSerializer

class AppUser(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class manufacturer(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class picture(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class stock(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class temperature(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class web_user(viewsets.ModelViewSet):
    queryset = WebUser.objects.all()
    serializer_class = WebUserSerializer

