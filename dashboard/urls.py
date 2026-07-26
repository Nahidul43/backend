from django.urls import path
from .views import (
    DashboardView,
    DepositCreateView,
    WithdrawCreateView,
    ProfileView,
    ApproveDepositView,
    RejectDepositView,
    AdminDepositListView,
    AdminWithdrawListView,
    ApproveWithdrawView,
    RejectWithdrawView,
    BuyProductView
)

urlpatterns = [

    path(
    "buy-product/<int:pk>/",
    BuyProductView.as_view()
),
path(
    "admin/deposits/",
    AdminDepositListView.as_view()
),

path(
    "admin/deposit/<int:pk>/approve/",
    ApproveDepositView.as_view()
),

path(
    "admin/deposit/<int:pk>/reject/",
    RejectDepositView.as_view()
),

path(
    "admin/withdraws/",
    AdminWithdrawListView.as_view()
),

path(
    "admin/withdraw/<int:pk>/approve/",
    ApproveWithdrawView.as_view()
),

path(
    "admin/withdraw/<int:pk>/reject/",
    RejectWithdrawView.as_view()
),



    path(
        "dashboard/",
        DashboardView.as_view()
    ),
    path(
    "deposit/",
    DepositCreateView.as_view()
),
path(
    "withdraw/",
    WithdrawCreateView.as_view()
),
path(
    "profile/",
    ProfileView.as_view()
),
path(
    "deposit/<int:pk>/approve/",
    ApproveDepositView.as_view()
),
path(
    "withdraw/<int:pk>/approve/",
    ApproveWithdrawView.as_view()
),
]