from django.db.models.fields import DateTimeField
from django.forms import widgets
from orders.models import Deliver, Message, Order
from django import forms


class OrderForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Order
        fields = ["price_offer", "deadline", "file_example", "order_message"]
        exclude = ["plan_id", "gig", "customer"]


class DeliverForm(forms.ModelForm):
    class Meta:
        model = Deliver
        fields = ["message", "file"]
        exclude = ["order", "is_accepted", "is_paid"]