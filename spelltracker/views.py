from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from spelltracker.forms import Character_Form
from spelltracker.models import Character
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)


class Index(ListView):
    model = Character
    template_name = 'index.html'


class Create(CreateView):
    model = Character
    template_name = 'create.html'
    form_class = Character_Form

    def get_success_url(self):
        return('/')


class Tracker(DetailView):
    model = Character
    template_name = 'tracker.html'
