import requests
from django.conf import settings
from django.shortcuts import render

from .beers import get_username_from_session


def search(request):
    username = get_username_from_session(request)
    search_param = request.GET.get('search')

    url = settings.WAREHOUSE_BACKEND + '/api/beers/'
    params = {
        'search': search_param,
    }
    result = requests.get(url, params=params)
    results = result.json()

    context = {
        'beers': results,
        'username': username,
    }
    return render(request, 'search.html', context)
