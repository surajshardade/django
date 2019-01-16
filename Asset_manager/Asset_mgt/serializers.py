from rest_framework import serializers
from Asset_mgt.models import Asset,Location,Category

class AssetSerializer_get(serializers.ModelSerializer):
    Location=serializers.CharField(source='Location.name',read_only=True)
    #print(Location)
    
    Category=serializers.CharField(source='Category.name',read_only=True)
    #print(Category)
    class Meta:
        model = Asset
        fields = ('ID', 'Label', 'Description', 'Location', 'Assignee','Category','SerialNo','model','warranty','image','ctime','mtime',)
        #owner = serializers.ReadOnlyField(source='owner.username')

class AssetSerializer(serializers.ModelSerializer):
    #Location=serializers.CharField(source='Location.name',read_only=True)
    #print(Location)
    
    #Category=serializers.CharField(source='Category.name',read_only=True)
    #print(Category)
    class Meta:
        model = Asset
        fields = ('ID', 'Label', 'Description', 'Location', 'Assignee','Category','SerialNo','model','warranty','image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=('ids','name','desc')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields=('ids','name','desc')