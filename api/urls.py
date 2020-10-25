from django.urls import path
from api import views

# products GET (single and list)
# contacts POST
# news GET (single and list)

urlpatterns = [
    path('news', views.NewsListAPIView.as_view(), name="news-list"),
    path('news/<int:id>', views.NewsDetailAPIView.as_view(), name="news-detail"),
    path('contact', views.CreateContactAPIView.as_view(), name="create-contant"),
    path('products', views.ProductListAPIView.as_view(), name="product-list"),
    path('products/<int:id>', views.ProductDetailAPIView.as_view(),
         name="product-detail"),
    path('products/featured', views.FeaturedProductsAPIView.as_view(),
         name="featured-products")
]
