from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class Show_all_posts(ListView):
    template_name = "blog/home.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3


class Newpost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/create-new-post.html"
    success_url = "/home/"

    def form_valid(self, form):
        form.instance.author = CustomUser.objects.get(user=self.request.user)
        form.save()
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/update-post.html"
    success_url = "/home/"


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete-post.html"
    success_url = "/home/"
