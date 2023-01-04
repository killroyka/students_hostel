from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from users.models import User


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'middle_name', 'room',
                  'hostel_number', 'contract_number', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(name, field)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(self.cleaned_data)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпали')
        if len(password1) < 8:
            raise forms.ValidationError('Пароль слишком короткий. Нужно минимум 8 символов')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}), label="Почта")

    class Meta:
        model = User
        fields = ('__all__',)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # self.fields["email"] = self.fields["username"]
        print(self.fields)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).first() is None:
            raise forms.ValidationError(
                "Такого пользователя нет. Учтите, что поля чувствительны к регистру.")
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user_cache = authenticate(self.request, username=email, password=password)
            if not user_cache:
                raise forms.ValidationError(
                    "Неверный пароль. Учтите, что поля чувствительны к регистру.")
        return password
