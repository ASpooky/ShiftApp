from django import forms
from .models import Users,ShiftDaily
from django.contrib.auth.password_validation import validate_password

class RegistForm(forms.ModelForm):
    username=forms.CharField(label="名前")
    age=forms.IntegerField(label="年齢",min_value=0)
    email=forms.EmailField(label="メールアドレス")
    password=forms.CharField(label="パスワード",widget=forms.PasswordInput())
    confirm_password=forms.CharField(label="パスワード再入力",widget=forms.PasswordInput())

    class Meta:
        model=Users
        fields=["username","age","email","password"]

    def save(self,commit=False):
        user=super().save(commit=False)
        validate_password(self.cleaned_data["password"],user)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
    
class ShiftChoiceForm(forms.ModelForm):
    shift_time=forms.fields.MultipleChoiceField(
        choices=(
            ("6:00~9:00","6:00~9:00"),
            ("9:00~14:00","9:00~14:00"),
            ("14:00~17:00","14:00~17:00"),
            ("17:00~22:00","17:00~22:00"),
            ("22:00~01:00","22:00~01:00"),
            ("01:00~","01:00~")
        ), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model=ShiftDaily
        fields=["shift_time"]

class UserLoginForm(forms.Form):
    email=forms.EmailField(label="メールアドレス")
    password=forms.CharField(label="パスワード",widget=forms.PasswordInput())
    