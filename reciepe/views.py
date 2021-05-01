from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reciepe


def reciepe_list(request):
    reciepes = Reciepe.objects.all()
    return render(request, 'reciepe/list.html', {'reciepes': reciepes})


def detail(request, Reciepe_id):
    rec_details = Reciepe.objects.get(id=Reciepe_id)
    return render(request, 'reciepe/home.html', {'rec_details': rec_details})


def create_reciepe(request):
    if request.method == "POST":
        reciepe = request.POST["reciepe_name"]
        ingradiants = request.POST["ingradiants"]
        process = request.POST["process"]
        Reciepe.objects.create(reciepe_name=reciepe, ingradiants=ingradiants, process=process)
        return HttpResponseRedirect("/reciepe/reciepe/")
    else:
        return render(request, "reciepe/create.html")
