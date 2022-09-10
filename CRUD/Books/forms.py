from django import forms
from Books.models import Books
class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class BookSearchForm(forms.Form):
    Book_Id = forms.IntegerField()
