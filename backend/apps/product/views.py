from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .models import Car
from .filters import CarFilter


class ProductView(FilterView):
    model = Car
    template_name = 'index.html'
    filterset_class = CarFilter
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SearchCarView(ListView):
    model = Car
    template_name = 'index.html'

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(name__icontains=search_text)
            | Q(description__icontains=search_text)

        )
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        return context


class DetailCarView(DetailView):
    template_name = 'car_detail.html'
