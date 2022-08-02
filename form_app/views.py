from xml.dom import INVALID_STATE_ERR
from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    return render(request, 'form_app/index.html')


def form(request):
    form = forms.form_view()

    if request.method == 'POST':
        form = forms.form_view(request.POST)

        if form.is_valid():
            print("Form values are")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'form_app/forms.html', {'form': form})


def user(request):
    form = forms.user_details()

    if request.method == 'POST':
        form = forms.user_details(request.POST)

        if form.is_valid():
            # print(form.cleaned_data['name'])
            form.save(commit=True)

    return render(request, 'form_app/user.html', {'form': form})
