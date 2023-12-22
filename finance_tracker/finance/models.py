from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Money(models.Model):
    """
        Модель отвечает за количество денег на балансе у пользователя
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Operation(models.Model):
    """
        Модель отвечает за операции (доход и расход)
    """

    CHOICES = (
        ('Питание', 'Food'),
        ('Развлечения', 'Games'),
        ('Медицина', 'Med'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    source = models.CharField(
        max_length=300,
        choices=CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user
