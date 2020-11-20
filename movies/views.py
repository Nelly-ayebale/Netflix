from django.shortcuts import render
import requests
import tmdbsimple as tmdb

tmdb.API_KEY= '2fe5b0203afe6f89a9ad311bd55df300'
# Create your views here.
def trailers(request,movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2fe5b0203afe6f89a9ad311bd55df300&append_to_response=videos')
    data = response.json()
    movies = data['videos']['results']
    return render(request,'trailers.html',{
        'overview' :data['overview'],
        'homepage' :data['homepage'],
        'videos' : movies,
        

    })

def home(request):
    popular_movies_tmdb = tmdb.Movies('popular')
    popular_movies = popular_movies_tmdb.info()['results']

    upcoming_movies_tmdb = tmdb.Movies('upcoming')
    upcoming_movies = upcoming_movies_tmdb.info()['results']

    return render(request,'movies.html',{'popular':popular_movies,'upcoming':upcoming_movies})

def single_movie(request,movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2fe5b0203afe6f89a9ad311bd55df300')
    movies = response.json()
    
   

    return render(request,'single_movie.html',{"movies":movies})