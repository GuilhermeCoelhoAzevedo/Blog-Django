from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(max_length=100, label='Email')
    assunto = forms.CharField(max_length=100, label="Assunto")
    mensagem = forms.CharField(widget=forms.Textarea, label="Mensagem")