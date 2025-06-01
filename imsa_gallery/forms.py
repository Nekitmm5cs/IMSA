from django import forms
from .models import MediaItem

class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'description', 'media_type', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MediaItemForm, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super(MediaItemForm, self).save(commit=False)
        if self.user:
            instance.uploaded_by = self.user
        if commit:
            instance.save()
        return instance