from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from accounts.models import User
from Products.models import Product

from dashboard.models import Wallet, Deposit, Withdraw
from .serializers import (
    DashboardUserSerializer,
    ProductSerializer,
    DepositSerializer,
    WithdrawSerializer,
)

from dashboard.models import Deposit, Withdraw, Wallet
from rest_framework.permissions import IsAdminUser


class AdminDepositListView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        deposits = Deposit.objects.filter(
            status="pending"
        )

        data = DepositSerializer(
            deposits,
            many=True
        ).data

        return Response(data)


class ApproveDepositView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request, pk):

        deposit = Deposit.objects.get(id=pk)

        if deposit.status == "pending":

            wallet, created = Wallet.objects.get_or_create(
                user=deposit.user
            )

            wallet.balance += deposit.amount
            wallet.save()

            deposit.status = "approved"
            deposit.is_added = True
            deposit.save()

        return Response({
            "message": "Deposit Approved"
        })


class RejectDepositView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request, pk):

        deposit = Deposit.objects.get(id=pk)

        deposit.status = "rejected"
        deposit.save()

        return Response({
            "message": "Deposit Rejected"
        })


class AdminWithdrawListView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        withdraws = Withdraw.objects.filter(
            status="pending"
        )

        data = WithdrawSerializer(
            withdraws,
            many=True
        ).data

        return Response(data)

class ApproveWithdrawView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request, pk):

        withdraw = Withdraw.objects.get(id=pk)

        wallet = Wallet.objects.get(
            user=withdraw.user
        )

        if wallet.balance >= withdraw.amount:

            wallet.balance -= withdraw.amount
            wallet.save()

            withdraw.status = "approved"
            withdraw.save()

        return Response({
            "message": "Withdraw Approved"
        })


class RejectWithdrawView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request, pk):

        withdraw = Withdraw.objects.get(id=pk)

        withdraw.status = "rejected"

        withdraw.save()

        return Response({
            "message": "Withdraw Rejected"
        })

class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        wallet, created = Wallet.objects.get_or_create(
            user=user,
            defaults={"balance": 0}
        )
        products = Product.objects.filter(
            assigned_user=user
        )

        deposits = Deposit.objects.filter(
            user=user
        )

        withdraws = Withdraw.objects.filter(
            user=user
        )

        product_value = sum(
            p.price for p in products
        )

        total_deposit = sum(
            d.amount
            for d in deposits.filter(
                status="approved"
            )
        )

        total_withdraw = sum(
            w.amount
            for w in withdraws.filter(
                status="approved"
            )
        )

        return Response({

            "user":
            DashboardUserSerializer(user).data,

            "wallet_balance":
            wallet.balance,

            "product_value":
            product_value,

            "total_products":
            products.count(),

            "total_deposit":
            total_deposit,

            "total_withdraw":
            total_withdraw,

            "products":
            ProductSerializer(
                products,
                many=True
            ).data,

            "deposits":
            DepositSerializer(
                deposits,
                many=True
            ).data,

            "withdraws":
            WithdrawSerializer(
                withdraws,
                many=True
            ).data,
        })

class DepositCreateView(generics.CreateAPIView):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WithdrawCreateView(generics.CreateAPIView):
    serializer_class = WithdrawSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        user = self.request.user

        has_products = Product.objects.filter(
            assigned_user=user
        ).exists()

        print("HAS PRODUCTS:", has_products)

        if has_products:
            raise ValidationError({
                "error": "You cannot withdraw while products are assigned to your account."
            })

        serializer.save(user=user)
    
    from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .serializers import ProfileSerializer


class ProfileView(
    generics.RetrieveUpdateAPIView
):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

from rest_framework.views import APIView
from rest_framework.response import Response

class ApproveDepositView(APIView):

    def post(self, request, pk):

        deposit = Deposit.objects.get(id=pk)

        if (
            deposit.status != "approved"
        ):

            deposit.status = "approved"

            wallet = Wallet.objects.get(
                user=deposit.user
            )

            wallet.balance += deposit.amount

            wallet.save()

            deposit.is_added = True

            deposit.save()

        return Response({
            "message":
            "Deposit Approved"
        })
    

class ApproveWithdrawView(APIView):

    def post(self, request, pk):

        withdraw = Withdraw.objects.get(
            id=pk
        )

        wallet = Wallet.objects.get(
            user=withdraw.user
        )

        if (
            wallet.balance
            >= withdraw.amount
        ):

            wallet.balance -= (
                withdraw.amount
            )

            wallet.save()

            withdraw.status = (
                "approved"
            )

            withdraw.save()

        return Response({
            "message":
            "Withdraw Approved"
        })


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Products.models import Product
from dashboard.models import Wallet


class BuyProductView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        user = request.user

        try:
            product = Product.objects.get(
                id=pk,
                assigned_user=user
            )
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=404
            )

        wallet = Wallet.objects.get(user=user)

        # commission add
        wallet.balance += product.commission
        wallet.save()

        # product remove from user
        product.delete()

        return Response({
            "message": "Product Completed",
            "commission": product.commission,
            "balance": wallet.balance
        })