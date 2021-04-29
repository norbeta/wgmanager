from django import forms
from .models import Key
#import wgconfig

class CustomKeyForm(forms.ModelForm):
    configField = forms.CharField(widget=forms.Textarea(attrs={'rows': 30, 'cols': 80}), required=False)

    def save(self, commit=True):
        configField = self.cleaned_data.get('configField', None)
        return super(CustomKeyForm, self).save(commit=commit)

    class Meta:
        model = Key
        fields = ['privatekey','publickey','ip4','ip6', 'configField']


class CreateKeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['group','peer','master','privatekey','publickey','ip4','ip6']
    
