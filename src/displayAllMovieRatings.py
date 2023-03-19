from prettytable import PrettyTable

# Import the Movie class from movie.py
from movie import Movie



def main():
    # Let's create some example movies with ratings
    movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 9)
    movie2 = Movie("The Godfather", "Francis Ford Coppola", 9)
    movie3 = Movie("The Dark Knight", "Christopher Nolan", 8)

    # Now let's add the movies to a list
    movies = [movie1, movie2, movie3]

    # Create the table with the headers and data
    table = PrettyTable()
    table.field_names = ["Title", "Director", "Rating"]
    for movie in movies:
        table.add_row([movie.title, movie.director, movie.rating])

    # Print the table
    print(table)

if __name__ == "__main__":
    main()
