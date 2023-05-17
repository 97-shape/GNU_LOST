from django.utils import timezone
from django.forms import inlineformset_factory

from django import forms
from .models import Post, Photo


class PostForm(forms.ModelForm):
    category = forms.ChoiceField(widget=forms.RadioSelect(attrs={"required": "required"}), choices=[("습득", "습득"), ("분실", "분실")])
    type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select', "required": "required"}), choices=[("카드/신분증","카드/신분증"),("지갑","지갑"),("전자기기","전자기기"),("의류","의류"),("기타","기타")])
    reward = forms.ChoiceField(widget=forms.RadioSelect(attrs={"required": "required"}), choices=[("0", "X"), ("1", "O")])
    writedate = forms.DateTimeField(widget=forms.HiddenInput, required=False)

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "required": "required"}))

    class Meta:
        model = Post
        fields = ['title', 'category', 'reward', 'type', 'content', 'writedate']

class PhotoForm(forms.ModelForm):
    src = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': False, 'class': 'form-control mb-3'}),
                              required=False)
    class Meta:
        model = Photo
        fields = ['src']

PhotoFormSet = inlineformset_factory(Post, Photo, form=PhotoForm, extra=8)
