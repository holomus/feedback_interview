from django.forms import ModelForm, TextInput, FileInput, Textarea
from feedback.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'title',
            'description',
            'attachment',
        ]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'attachment': FileInput()
        }
