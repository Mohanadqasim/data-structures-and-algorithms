def sort_by_year(movies):
    """
    Sorts a list of movies based on their year in ascending order.
    Args:movies (list): A list of dictionaries representing movies.
    Returns:list: The sorted list of movies.
    """
    for i in range(len(movies) - 1):
        for j in range(i + 1, len(movies)):
            if movies[i]['year'] > movies[j]['year']:
                movies[i], movies[j] = movies[j], movies[i]
    return movies


def remove_leading_words(title, words):
    """
    Removes leading words from a movie title.
    Args:title (str): The title of the movie, words (list): A list of words to be removed from the title.
    Returns:str: The title with leading words removed.
    """
    title_words = title.split()
    while len(title_words) > 0 and title_words[0] in words:
        title_words.pop(0)
    return ' '.join(title_words)


def sort_alphabetically(movies):
    """
    Sorts a list of movies alphabetically, considering leading word removal.
    Args:movies (list): A list of dictionaries representing movies.
    Returns:list: The sorted list of movies.
    """
    ignore_words = ["A", "An", "The"]
    for i in range(len(movies) - 1):
        for j in range(i + 1, len(movies)):
            title_a = remove_leading_words(movies[i]['title'], ignore_words)
            title_b = remove_leading_words(movies[j]['title'], ignore_words)
            if title_a.lower() > title_b.lower():
                movies[i], movies[j] = movies[j], movies[i]
            elif title_a.lower() == title_b.lower():
                if movies[i]['title'].lower() > movies[j]['title'].lower():
                    movies[i], movies[j] = movies[j], movies[i]
                elif movies[i]['title'].lower() == movies[j]['title'].lower():
                    if movies[i]['title'] > movies[j]['title']:
                        movies[i], movies[j] = movies[j], movies[i]
    return movies


movies = [
    {"title": "The Dark Knight", "year": 2008},
    {"title": "Pulp Fiction", "year": 1994},
    {"title": "Inception", "year": 2010},
    {"title": "The Shawshank Redemption", "year": 1994},
    {"title": "The Godfather", "year": 1972},
    {"title": "Avatar", "year": 2009},
    {"title": "Blade Runner", "year": 1982},
    {"title": "Casablanca", "year": 1942},
    {"title": "Django Unchained", "year": 2012},
    {"title": "E.T. the Extra-Terrestrial", "year": 1982},
    {"title": "Fight Club", "year": 1999},
    {"title": "Gladiator", "year": 2000},
    {"title": "Harry Potter and the Philosopher's Stone", "year": 2001},
    {"title": "Inglourious Basterds", "year": 2009},
    {"title": "Jaws", "year": 1975},
    {"title": "Kill Bill: Volume 1", "year": 2003},
    {"title": "La La Land", "year": 2016},
    {"title": "Memento", "year": 2000},
    {"title": "No Country for Old Men", "year": 2007},
    {"title": "The Omen", "year": 1976},
    {"title": "Pan's Labyrinth", "year": 2006},
    {"title": "Quantum of Solace", "year": 2008},
    {"title": "Raiders of the Lost Ark", "year": 1981},
    {"title": "The Social Network", "year": 2010},
    {"title": "Titanic", "year": 1997},
    {"title": "Unforgiven", "year": 1992},
    {"title": "Vertigo", "year": 1958},
    {"title": "The Wizard of Oz", "year": 1939},
    {"title": "X-Men", "year": 2000},
    {"title": "Young Frankenstein", "year": 1974},
    {"title": "Zootopia", "year": 2016}
]
# print(sort_by_year(movies))
print(sort_alphabetically(movies))
