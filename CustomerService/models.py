from django.db import models
from django.conf import settings


class SupportTicket(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("solved", "Solved"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tickets"
    )

    subject = models.CharField(max_length=255)

    message = models.TextField()

    admin_reply = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject