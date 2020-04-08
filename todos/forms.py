from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('categorie','important_level','content','time','user_id')
        labels = {
            'categorie':'Kategori',
            'important_level':'Önem derecesi',
            'content':'İçerik',
            'time':'Verilen süre'
        }
