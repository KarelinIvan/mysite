from django import forms


class EditPostForm(forms.Form):
    """ Форма для отправки поста по e-mail """
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
