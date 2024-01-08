from django import forms

from core.models import Cart


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('owner', 'product')
