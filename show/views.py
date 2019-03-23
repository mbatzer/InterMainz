# from django.shortcuts import render
from django.views.generic import ListView
from .models import ShowPicture


class ShowListView(ListView):
    model = ShowPicture
    context_object_name = 'photos'


# def home(request):
#     return render(request, 'show/showpicture_list.html')
