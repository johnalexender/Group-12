
from django.db import models

class Investment(models.Model):
    member_name = models.CharField(max_length=100)
    member_cpm = models.CharField(max_length=100)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.member_name} - {self.investment_amount}'
