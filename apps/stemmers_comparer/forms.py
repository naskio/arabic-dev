from django import forms
import json


class FilterLanguagesForm(forms.Form):
    languages = forms.CharField(required=False)

    def get_languages(self):
        txt = str(self.cleaned_data.get('languages'))
        ls = []
        if txt:
            ls = json.loads(txt)
        return ls


class PostReviewForm(forms.Form):
    comment = forms.CharField(required=True)
    score = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1, 6)])
    user_email_address = forms.EmailField(required=True)
    user_github_account_link = forms.URLField(required=False)
