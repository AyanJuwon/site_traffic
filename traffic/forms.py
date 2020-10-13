from django import forms

class SiteUrl(forms.Form):
    site_url = forms.CharField(max_length=100)