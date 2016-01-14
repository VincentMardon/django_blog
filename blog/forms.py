from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('pseudo', 'email', 'contenu')
        
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        
        if len(cleaned_data) < 3:
            raise forms.ValidationError('Veuillez remplir tous les champs.')
        
        return cleaned_data