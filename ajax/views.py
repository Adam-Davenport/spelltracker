from django.shortcuts import render
from django.http import JsonResponse


def update_tracker(request):
    data = {
        'test': 'test data'
    }
    return JsonResponse(data)
