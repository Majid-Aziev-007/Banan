from django.contrib.auth import get_user_model
from django.forms import ModelForm

from .models import Operation

class OperationForm(ModelForm):
    class Meta:

        model = Operation

        fields = ('amount', 'source')
