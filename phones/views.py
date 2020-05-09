from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView
from .models import Abonent
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

# ...
 
class HomePageView(ListView):
    model = Abonent
    context_object_name = 'abonents'
    template_name = 'home.html'
 
    def get_queryset(self):
        abonents = Abonent.objects.all()
        # Отбираем первые 10 статей
        paginator = Paginator(abonents, 10)
        page = self.request.GET.get('page')
        try:
            abonents = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            abonents = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            abonents = paginator.page(paginator.num_pages)
        return abonents

# поисковая строка
class SearchResultsView(ListView):
    model = Abonent
    template_name = 'search_results.html'

    def get_queryset(self): 
        try:
            query = self.request.GET.get('q')
            objects_list = Abonent.objects.filter(
                Q(rank__icontains=query) | Q(name__icontains=query)
                )
            return objects_list
        except Abonent.DoesNotExist:
            return HttpResponseNotFound("<h2>Абонент не найден</h2>")

# сохранение данных в бд
def create(request):
    if request.method=="POST":
        objects_list = Abonent()
        objects_list.rank = request.POST.get("rank")
        objects_list.name = request.POST.get("name")
        objects_list.phone = request.POST.get("phone")
        objects_list.IP_phone = request.POST.get("IP_phone")
        objects_list.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):

    try:
        objects_list = Abonent.objects.get(id=id)
        if request.method=="POST":
            objects_list.rank = request.POST.get("rank")
            objects_list.name = request.POST.get("name")
            objects_list.phone = request.POST.get("phone")
            objects_list.IP_phone = request.POST.get("IP_phone")
            objects_list.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"Abonent": Abonent})
    except Abonent.DoesNotExist:
        return HttpResponseNotFound("<h2>Абонент не найден</h2>")
     # button back

def button_back(request):
    return render(request, "home.html", {"Abonent": Abonent})

# удаление данных из бд
def delete(request, id):
    try:
        objects_list = Abonent.objects.get(id=id)
        objects_list.delete()
        return HttpResponseRedirect("/")
    except Abonent.DoesNotExist:
        return HttpResponseNotFound("<h2>Абонент не найден</h2>")



