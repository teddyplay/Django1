from django.shortcuts import render
from.models import Director, Movie, Review


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




def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {'movie': movie_list}
    return render(request, 'movie_list.html', context=context)

def movie_detail_view(request, id):
    movie_list = Movie.objects.get(id=id)
    director = Director.objects.filter(id=id)
    review = Review.objects.filter(id=id)
    context = {'movie': movie_list,'director': director, 'review': review}
    return render(request, 'movie_detail.html', context=context)

def director_list_view(request):
    list = Director.objects.all()
    context = {'director': list}
    return render(request, 'director_list.html', context=context)

def director_detail_view(request, id):
    list = Director.objects.get(id=id)
    context = {'director': list}
    return render(request, 'director_detail.html', context=context)

def review_list_view(request):
    list = Review.objects.all()
    context = {'review': list}
    return render(request, 'review_list_view.html', context=context)

def review_detail_view(request, id):
    list = Review.objects.get(id=id)
    context = {'review': list}
    return render(request, 'review_detail_view.html', context=context)





