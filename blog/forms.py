from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-auto border rounded p-2',
                'placeholder': 'Το όνομά σου'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-auto border rounded p-2',
                'placeholder': 'Το email σου'
            }),
            'body': forms.Textarea(attrs={
                'class': 'w-auto border rounded p-2',
                'placeholder': 'Το σχόλιό σου'
            }),
        }