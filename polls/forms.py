from django import forms


class AnswerForm(forms.Form):
    rebus_id = forms.IntegerField(label='ID')
    word1 = forms.CharField(label='Слово 1', max_length=100)
    word2 = forms.CharField(label='Слово 2', max_length=100)
    word3 = forms.CharField(label='Слово 3', max_length=100)

