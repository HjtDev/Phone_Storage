from django import forms
from .models import Phone, Brand

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'price', 'color', 'display_size', 'made_in', 'is_available']

    def clean_brand(self):
        brand_name = self.cleaned_data['brand']
        if not brand_name:
            raise forms.ValidationError("Brand Name is required.")
        return brand_name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is None or price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color:
            raise forms.ValidationError("Color is required.")
        return color

    def clean_display_size(self):
        display_size = self.cleaned_data['display_size']
        if display_size is None or display_size <= 0:
            raise forms.ValidationError("Display Size must be a positive integer.")
        return display_size

    def clean_made_in(self):
        made_in = self.cleaned_data['made_in']
        if not made_in:
            raise forms.ValidationError("Made In is required.")
        return made_in
