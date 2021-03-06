from django import forms


class EmailerForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    seconds = forms.IntegerField(min_value=0)
    to_whom = forms.EmailField()

    subject.widget.attrs.update({'class': 'form-control'})
    message.widget.attrs.update({'class': 'form-control'})
    seconds.widget.attrs.update({'class': 'form-control'})
    to_whom.widget.attrs.update({'class': 'form-control'})
