from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={ 
        }
        return render(request, 'pages/index.html', context)

def get_data(request, *args, **kwargs):
    data = {
        'manuel': 2,
        'sergio': 3,
        'pablo': 4,
    }
    return JsonResponse(data)