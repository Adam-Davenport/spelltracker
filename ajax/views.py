from django.shortcuts import render
from django.http import JsonResponse
from spelltracker.models import Character


def update_spells(request):
    characterid = request.GET.get('characterid', None)
    prepared = request.GET.getlist('prepared[]', None)
    spent = request.GET.getlist('spent[]', None)
    character = Character.objects.get(id=characterid)
    character.AjaxUpdate(prepared, spent)
    data = {
        'prepared': [character.l1p, character.l2p, character.l3p]
    }
    return JsonResponse(data)
