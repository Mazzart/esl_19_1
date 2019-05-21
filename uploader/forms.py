from django import forms
from uploader.models import Document


class DocumentForm(forms.ModelForm):
    """Class for form fields"""

    class Meta:
        model = Document
        fields = ('file', 'time')
        help_texts = {'file': 'Select file:',
                      'time': 'Enter the lifetime of the file (number of seconds):'}
