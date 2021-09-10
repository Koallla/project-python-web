from django import forms
from . models import Note, Tag

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'value', 'tags']

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner')
        super(NoteCreateForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Note.objects.filter(owner=self.owner, title=title).exists():
            raise forms.ValidationError("You have already written a note with same title.")
        return title
        
class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'value', 'tags']
        
class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if Tag.objects.filter(title=title).exists():
            raise forms.ValidationError("You have already written a tag with same title.")
        return title