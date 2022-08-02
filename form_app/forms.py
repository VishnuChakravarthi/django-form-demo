from django import forms
from django.core import validators
from form_app.models import UserDetail


class form_view(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])


class user_details(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = "__all__"

    def clean(self):
        super(user_details, self).clean()

        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']

        if len(name) < 4:
            self._errors['name'] = self.error_class(['Minimum 4 letters'])

        if len(str(phone)) < 10:
            self._errors['phone'] = self.error_class(['Length should be 10'])

        return self.cleaned_data
