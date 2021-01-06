from django.db import models
from django.contrib.auth.models import User

class TRACKER(models.Model):
    action_choices = [
        ('Credited','Credited by'),
        ('Debited','Debited by'),
    ]
    amount_choices = [
        ('dollar','💲'),
        ('rupee','₹'),
    ]
    title = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    amount_sign = models.CharField(max_length=10,choices=amount_choices)
    action = models.CharField(max_length=10,choices=action_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

