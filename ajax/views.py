from django.shortcuts import render
from django.http import JsonResponse


def update_spells(request):
    characterid = request.GET.get('characterid', None)
    print(characterid)
    data = {
        'test': 'test data'
    }
    return JsonResponse(data)
