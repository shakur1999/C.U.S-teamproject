from django.forms import ModelForm
from .models import cusapp


class cusform(ModelForm):
    class Meta:
        model = cusapp
        fields = ['title', 'description', 'location']

class cusform(ModelForm):
    class Meta:
        model = cusapp
        fields = ['title', 'description', 'location']



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
