from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

    title = forms.CharField(widget=forms.TextInput(attrs=({'placeholder': 'title'})))
    text = forms.CharField(widget=forms.Textarea(attrs=({'placeholder': 'title'})))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-8 m-2')
            ),
            Row(
                Column('text', css_class='form-group col-md-8 m-2')
            ),
            Row(
                Submit('submit', 'save', css_class="m-3")
            )
        )


