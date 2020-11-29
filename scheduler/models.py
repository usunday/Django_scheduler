from django.db import models

# Create your models here.
class Member(models.Model):
    """Model represent Members """
    nickName = models.CharField(max_length=30)
    email = models.CharField(max_length=255, help_text='Email address for email notification')

    def __str__(self):
        """model object to String"""
        return f'name={self.nickName}'

class ServingDay(models.Model):
    """Model represent Day of Serving"""
    server = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True, help_text='Serving member for day')
    date = models.DateField(null=True, blank=True)
    memo = models.TextField(max_length=1024)

    def __str__(self):
        """model object to String"""
        return f'date:{self.date}'
