from django import forms
from django.contrib.auth.forms import UserCreationForm

from cooking.models import Recipe, User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'text', 'level', 'image')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
