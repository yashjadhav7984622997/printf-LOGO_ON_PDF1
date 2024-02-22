# pdf_logo/forms.py
from django import forms

class LogoForm(forms.Form):
    pdf_file = forms.FileField(label='Select PDF file')
    logo = forms.ImageField(label='Select logo')