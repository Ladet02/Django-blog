from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comment',
        'id': 'comment',
        'rows': '4',
        'aria-hidden': 'true'
    }))

    class Meta:
        model = Comment
        fields = ('content', )
