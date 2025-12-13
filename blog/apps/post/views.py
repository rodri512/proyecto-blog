from django.views.generic import TemplateView

class PostList(TemplateView):
    template_name='post/post-list.html'
