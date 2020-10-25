from rest_framework import generics, permissions
from api.serializers import ContactSerializer, ProductSerializer, NewsSerializer
from api.models import News, Contact, Product


class NewsListAPIView(generics.ListAPIView):
    """
    News List
    """
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()


class NewsDetailAPIView(generics.RetrieveAPIView):
    """
    News Detail (single news)
    """
    serializer_class = NewsSerializer
    lookup_field = "id"

    def get_queryset(self):
        return News.objects.all()


class CreateContactAPIView(generics.CreateAPIView):
    """
    Contact create
    """
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.all()


class ProductListAPIView(generics.ListAPIView):
    """
    products List
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
product Details
    """
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Product.objects.all()


class FeaturedProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(featured=True)
