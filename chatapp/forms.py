from django import forms

class SendMessageForm(forms.Form):
    content = forms.CharField(label='메시지', widget=forms.Textarea(attrs={'rows': 3}))

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) == 0:
            raise forms.ValidationError('메시지를 입력해주세요.')
        return content