from django.views.generic import ListView, DetailView
from .models import Player


class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    ordering = 'first_name'


class PlayerDetailView(DetailView):
    model = Player
