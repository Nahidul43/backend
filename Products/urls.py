# from django.urls import path
# from .views import (
#     ProductListCreateView,
#     ProductRetrieveUpdateDestroyView,
#     MyProductsView,
# )

# urlpatterns = [
#     path("", ProductListCreateView.as_view()),
#     path("<int:pk>/", ProductRetrieveUpdateDestroyView.as_view()),
# ]

from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    MyProductsView,
    PublicProductListView
)

urlpatterns = [
    path(
        "",
        ProductListCreateView.as_view(),
        name="products",
    ),
  path(
        "public/",
        PublicProductListView.as_view(),
        name="public-products",
    ),
    path(
        "<int:pk>/",
        ProductRetrieveUpdateDestroyView.as_view(),
        name="product-detail",
    ),

    path(
        "my-products/",
        MyProductsView.as_view(),
        name="my-products",
    ),
]