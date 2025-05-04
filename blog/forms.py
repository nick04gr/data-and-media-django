from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Το όνομά σου',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Το email σου',
        })
    )
    to = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full border border-gray-300 rounded px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Παραλήπτης email',
        })
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full border border-gray-300 rounded px-4 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Πρόσθετα σχόλια (προαιρετικά)',
            'rows': 4
        })
    )

    
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