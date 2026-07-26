from rest_framework import serializers
from .models import SupportTicket


class SupportTicketSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    class Meta:
        model = SupportTicket
        fields = "__all__"
        read_only_fields = (
            "user",
            "admin_reply",
            "status",
        )