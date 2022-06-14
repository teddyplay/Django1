from django.shortcuts import render


# Create your views here.

def index(request):
    dict_ = {
        'key': 'Погода хмурая))',
        'color': 'red'
    }

    return render(request, 'index.html', context=dict_)


def joy(request):
    return render(request, 'joy.html')


def sad(request):
    return render(request, 'sad.html')
