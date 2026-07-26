from django.urls import path
from .views import (
    UserTicketListCreateView,
    AdminTicketListView,
    AdminReplyTicketView,
)

urlpatterns = [
    path(
        "tickets/",
        UserTicketListCreateView.as_view()
    ),

    path(
        "admin/tickets/",
        AdminTicketListView.as_view()
    ),

    path(
        "admin/tickets/<int:pk>/",
        AdminReplyTicketView.as_view()
    ),
]