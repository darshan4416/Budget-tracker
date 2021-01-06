from django.forms import ModelForm
from .models import TRACKER

class TRACKERForm(ModelForm):
    class Meta:
        model = TRACKER
        fields = ['title','amount_sign','amount','action']