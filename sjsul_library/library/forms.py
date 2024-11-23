from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LibraryUser
from .models import Role

class LibraryUserCreationForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)
    
    class Meta:
        model = LibraryUser
        fields = ('role',)  # Add other fields if needed
