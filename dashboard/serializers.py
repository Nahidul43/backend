from rest_framework import serializers
from accounts.models import User
from Products.models import Product
from .models import Wallet, Deposit, Withdraw

class DashboardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "unique_id",
            "full_name",
            "username",
            "email",
            "phone",
            "address",
            "profile_pic",
            "nid_image",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"
        read_only_fields = ["user", "status"]
class WithdrawSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdraw
        fields = "__all__"
        read_only_fields = ["user", "status"]


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "unique_id",
            "full_name",
            "username",
            "email",
            "phone",
            "address",
            "profile_pic",
            "nid_image",
        ]

        read_only_fields = [
            "unique_id",
            "email",
        ]