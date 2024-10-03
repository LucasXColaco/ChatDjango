from django import forms

class Register(forms.Form):
    usuario = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

class Login(forms.Form):
    usuario = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)

class Chat(forms.Form):
    mensagem = forms.CharField(widget=forms.TextInput(attrs={'id': 'mensagem-form', 'autocomplete': 'off'}), label='')