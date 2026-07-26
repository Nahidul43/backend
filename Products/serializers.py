from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):

    unique_id = serializers.CharField(
        write_only=True,
        required=False
    )

    image = serializers.ImageField(
        required=False
    )

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["assigned_user"]

    def create(self, validated_data):

        unique_id = validated_data.pop(
            "unique_id",
            None
        )

        if not unique_id:
            raise serializers.ValidationError({
                "unique_id": "User Unique ID is required"
            })

        try:
            user = User.objects.get(
                unique_id=unique_id
            )

        except User.DoesNotExist:

            raise serializers.ValidationError({
                "unique_id": "Invalid User Unique ID"
            })

        validated_data["assigned_user"] = user

        return Product.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):

        # update এর সময় unique_id ignore করবে
        validated_data.pop(
            "unique_id",
            None
        )

        for attr, value in validated_data.items():
            setattr(
                instance,
                attr,
                value
            )

        instance.save()

        return instance