from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


class SearchFilmView(generic.ListView):
    template_name = 'show.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Films.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


#get id
def film_detail(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Films, id=id)
        return render(
            request,
            template_name='show_detail.html',
            context={
                'film_id': film_id,
            }
        )


#list
@method_decorator(cache_page(60*15), name='dispatch')
class FilmListView(generic.ListView):
    template_name = 'show.html'
    model = models.Films
    context_object_name = 'query'

    def get_queryset(self):
        films = cache.get('query')
        if not films:
            films = self.model.objects.all()
            cache.set('query', films)
        return films




# def films_list(request):
#     if request.method == 'GET':
#         query = models.Films.objects.all()
#         return render(
#             request,
#             template_name='show.html',
#             context={
#                 'query': query,
#             }
#         )




def emodji(request):
    if request.method == "GET":
        return HttpResponse("🧠")


def text(request):
    if request.method == "GET":
        return HttpResponse("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

def image(request):
    if request.method == "GET":
        return HttpResponse("<img src='https://cdn.trinixy.ru/pics6/20230801/240813_1_trinixy_ru.jpg'>")