from django import forms
from .models import Car, Brand, Comment


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = "__all__"
        exclude = ['owner']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']


class OrderForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
