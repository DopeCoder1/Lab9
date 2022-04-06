from django import forms
from .models import Message
from .wigdet import DatePickerInput,TimePickerInput,DateTimePickerInput

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'phone','emails','mssg','dates')
        widgets = {
            'dates': DatePickerInput(),
        }