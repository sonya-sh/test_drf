from django.contrib.auth.models import AbstractUser, Group
from django.db import models

"""
Если бд ещё пустая, закомментировать строку админ в настройках и путь в urls,
сделать миграции с моделью кастом юзера, раскомментировать строки и сделать миграцию еще раз
"""
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    #user_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username