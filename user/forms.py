from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="İstifadəçi adı")
    password = forms.CharField(max_length=50, label="Şifrə", widget=forms.PasswordInput)
    confirm =  forms.CharField(max_length=50, label="Şifrə təkrar")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm =  self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Şifrələr uyğun deyil!!!")
        