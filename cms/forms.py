from django.views.generic.edit import CreateView
from api.models import Content

class AuthorCreate(CreateView):
    model = Content
    fields = ['owner']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)