from django.views.generic import TemplateView
from .models import Books

class BooksView(TemplateView):
    template_name = "books_portal/index.html"

    def get_context_data(self, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        books_list = list(Books.objects.all())
        context.update({
            'books_list': books_list,
        })

        return context

class AddView(TemplateView):
    template_name = "books_portal/add.html"

class DetailsView(TemplateView):
    template_name = "books_portal/details.html"