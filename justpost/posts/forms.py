from django import forms
from posts.models import Post

from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        labels = {
            "titulo": _("Título"),
            "conteudo": _("Conteúdo"),
        }
        help_texts = {
            "conteudo": _("Formatação com <strong>**Markdown**</strong> está <em>_disponível,_</em> experimente!")
        }
