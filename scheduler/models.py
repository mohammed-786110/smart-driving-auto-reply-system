from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    relation = models.CharField(max_length=50)
    auto_reply_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ScheduledMessage(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message = models.TextField()
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    sent_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.contact.name} - {self.status}"


class UserState(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driving = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Driving: {self.is_driving}"


class MessageLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
