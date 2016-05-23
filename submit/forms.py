from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    CHOICES=(('var','variants sheet',), ('pub', 'publications sheet',), ('ind', 'individuals sheet'),('all','All information'))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
