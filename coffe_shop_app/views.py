from django.http import HttpResponse
from django.views import generic
from .forms import ProductForm
from django.urls import reverse_lazy

class ProductFormViews(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)