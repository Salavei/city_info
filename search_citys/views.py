from django.shortcuts import render
from .parsing_info import start_parse
from .forms import CityForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            try:
                context = start_parse(request.POST['name_city'])
                context['name'] = request.POST['name_city']
                return render(request, 'search_citys/info.html', context)
            except AttributeError:
                messages.error(request, 'Города не существует')
                return render(request, 'search_citys/home.html', {'form': form})
    form = CityForm()
    return render(request, 'search_citys/home.html', {'form': form})
