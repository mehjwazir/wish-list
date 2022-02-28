from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

# Create your views here.


class WishList(ListView):
    model = Wish


class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'


class WishDelete(DeleteView):
    model = Wish
    success_url = '/'
