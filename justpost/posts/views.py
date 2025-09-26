from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from posts.models import Post
from posts.forms import PostForm


class PostListView(ListView):
    ''' View para listar todos os posts '''
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    ''' View para exibir os detalhes de um post '''
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    ''' View para criar um novo post '''
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    # Redireciona para a página de detalhes do post após a criação
    def get_success_url(self):
        return reverse_lazy('posts:post-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Define o autor do post como o usuário que está logado
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    ''' View para editar um post existente '''
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    # Redireciona para a página de detalhes do post após a edição
    def get_success_url(self):
        return reverse_lazy('posts:post-detail', kwargs={'pk': self.object.pk})

    # Garante que apenas o autor do post possa editá-lo
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    ''' View para deletar um post '''
    model = Post
    template_name = 'posts/post_delete.html'

    # Redireciona para a lista de posts após a deleção
    def get_success_url(self):
        return reverse_lazy('posts:post-list')

    # Garante que apenas o autor do post possa deletá-lo
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor
