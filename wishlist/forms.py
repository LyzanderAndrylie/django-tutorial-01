from dataclasses import field
from wishlist.models import BarangWishlist
from django import forms

class BarangWishlistForm(forms.ModelForm):

    class Meta:
        model = BarangWishlist
        fields = ("__all__")