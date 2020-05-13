from django import forms
from .models import Contact,Rent


class ContactForm(forms.ModelForm):
    Name = forms.CharField(required=True)
    From_Email = forms.EmailField(required=True)
    Message = forms.CharField(widget=forms.Textarea,required=True)

    class Meta:
        model = Contact
        fields = ('Name','From_Email','Message',)


class RentedForm(forms.ModelForm):
    Name = forms.EmailField(required=True)
    class Meta:
        model = Rent
        fields = ('Name',)
