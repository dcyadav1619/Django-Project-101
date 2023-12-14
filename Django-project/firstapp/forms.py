from django import forms

class PostForm(forms.Form):
    image = forms.ImageField()
    text = forms.CharField(label="Description")
    