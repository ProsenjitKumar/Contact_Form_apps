from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=40, help_text='100 Character Max.')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)

    