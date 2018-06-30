from django import forms
from .models import cusapp


class cusform(forms.ModelForm):
    class Meta:
        model = cusapp
        fields = ['title', 'description', 'location']
    title = forms.CharField(
        label = 'Title',
        max_length = 255,
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'title'}
        )
    )

    description = forms.CharField(
        label = 'Body',
        max_length = 255,
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'description'}
        )
    )

    location = forms.CharField(
        label = 'Location',
        max_length = 255,
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'name': 'location'}
        )
    )




# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
#
# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']
#


# class cusform(ModelForm):
#     class Meta:
#         model = cusapp
#         field = ["title", "description"],
#
#
#
# from django.forms import ModelForm
# from .models import cusapp
#
# class cusform(ModelForm):
#     class Meta:
#         model = cusapp
#         fields = ["title", "description"],
#         fields = '__all__'
#         # include = ["title", "description"],
