import requests
import json
from decouple import config


# Get a key on https://www.omdbapi.com/
key = config("SECRET_KEY")

while True:

    search_movie = input('Enter a movie: ')
    # It can be filtered by other parameters.
    params = {
        's': search_movie,
    }

    movie_request = requests.get(f'http://www.omdbapi.com/?apikey={key}&s={search_movie}&type=movie')

    try:
        movie = movie_request.json()['Search']
        
        for item in movie:
            print(item['Title'])

        print()        

    except KeyError:    
        print(f'My bad. I cannot find this one.\n')

    else:
        try:
            search_title = input('Search for a movie title and get more info about it: \n')

            title_request = requests.get(f'http://www.omdbapi.com/?apikey={key}&t={search_title}&type=movie')
            title = title_request.json()

            print(f"Title: {title['Title']}")
            print(f"Year: {title['Year']}")
            print(f"Runtime: {title['Runtime']}")
            print(f"Genre: {title['Genre']}")
            print(f"Director: {title['Director']}")
            print(f"Actors: {title['Actors']}")
            print(f"Plot: {title['Plot']}")
            print(f"Poster: {title['Poster']}\n")

        except KeyError:    
            print(f"In this case, you need to enter the exact movie's title.\n")

    finally:        
        next_movie = input('Do you want to search another one? [Y] Yes or any key to exit. \n')
        
        if next_movie.lower() != 'y':
            break

    













