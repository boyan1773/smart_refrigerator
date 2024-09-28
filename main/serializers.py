from rest_framework import serializers
from .models import (AppUser,AuthGroup,AuthGroupPermissions,AuthPermission,
    AuthUser,AuthUserGroups,AuthUserUserPermissions,DjangoAdminLog,DjangoContentType
    ,DjangoMigrations,DjangoSession,Manufacturer,Picture,Stock,Temperature,WebUser,
)

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'

class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'

class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'

class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'

class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'

class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'

class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUser
        fields = '__all__'
