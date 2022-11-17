class Movie:
    __watched_movies = 0

    def __init__(self, name, director):
        name = name
        director = director
        watched = False

    def change_name(self, new_name: str):
        name = new_name

    def change_director(self, new_director: str):
        director = new_director

    def watch(self):
        if watched == False:
            watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f'Movie name: {name}; Movie director: {director}. Total watched movies: {Movie.__watched_movies}'

first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)

