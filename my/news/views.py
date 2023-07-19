from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .serializers import MyModelSerializer
from rest_framework import generics
def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = Artiles.objects.all()
    serializer_class = MyModelSerializer

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верной'
    form = ArtilesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)