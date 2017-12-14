from django.shortcuts import render
from django.http import JsonResponse
from spelltracker.models import Character


def update_spells(request):
    characterid = request.GET.get('characterid', None)
    prepared = request.GET.get('prepared', None)
    print(request.GET)
    print(prepared)
    character = Character.objects.get(id=characterid)
    print(character)
    data = {
        'prepared': [character.l1p, character.l2p, character.l3p]
    }
    return JsonResponse(data)
