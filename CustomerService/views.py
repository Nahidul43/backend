from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import SupportTicket
from .serializers import SupportTicketSerializer


class UserTicketListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = SupportTicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SupportTicket.objects.filter(
            user=self.request.user
        ).order_by("-id")

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


from Products.permissions import IsAdminUserOnly

class AdminTicketListView(
    generics.ListAPIView
):

    serializer_class = SupportTicketSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUserOnly
    ]

    queryset = SupportTicket.objects.all().order_by("-id")



from rest_framework.views import APIView
from rest_framework.response import Response


class AdminReplyTicketView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserOnly
    ]

    def patch(self, request, pk):

        ticket = SupportTicket.objects.get(
            id=pk
        )

        ticket.admin_reply = request.data.get(
            "admin_reply"
        )

        ticket.status = "solved"

        ticket.save()

        return Response({
            "message": "Ticket solved"
        })