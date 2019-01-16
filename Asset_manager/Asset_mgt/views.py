from django.shortcuts import render

# Create your views here.
from Asset_mgt.models import Asset,Category,Location
from Asset_mgt.serializers import AssetSerializer,AssetSerializer_get,CategorySerializer, LocationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AssetList(APIView):
    """
    List all assets, or create a new asset.
    """
    def get(self, request, format=None):
        Assets = Asset.objects.all()
        serializer = AssetSerializer_get(Assets, many=True)
        return Response(serializer.data)
        #return Response('{"status"="success"}')

    def post(self, request, format=None):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDetail(APIView):
    """
    Retrieve, update or delete a asset instance.
    """
    def get_object(self, pk):
        try:
            return Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Asset = self.get_object(pk)
        serializer = AssetSerializer_get(Asset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Asset = self.get_object(pk)
        serializer = AssetSerializer(Asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Asset = self.get_object(pk)
        Asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):
    """
    List all Category, or create a new Category.
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
        #return Response('{"status"="success"}')

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationList(APIView):
    """
    List all Category, or create a new Category.
    """
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
        #return Response('{"status"="success"}')

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
