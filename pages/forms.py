from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message', 'attachment']

    def clean_attachment(self):
        file = self.cleaned_data.get('attachment')
        if file and file.size > 1 * 1024 * 1024:
            raise forms.ValidationError("الملف يجب ألا يتجاوز 1MB")
        return file