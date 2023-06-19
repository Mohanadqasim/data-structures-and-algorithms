# Problem Domain:

### Write two functions:

* sort_by_year: takes an object of movies, the object contains information about each movie (title, release year, genre) and returns an object but the movies are sorted according to release year

* sort_alphabetically: takes an object of movies, the object contains information about each movie (title, release year, genre) and returns an object but the movies are sorted alphabetically(title). The function ignores ("A"s, "An"s, "The"s) if founded at the beginning of the title.

# Big O:
sort_by_year:

    Time = O(n^2)
    Space = O(1)

sort_alphabetically:

    Time = O(n^2)
    Space = O(1)

remove_leading_words:

    Time = O(m)
    Space = O(1)

# Solution:
sort_by_year:
```
def sort_by_year(movies):
    for i in range(len(movies) - 1):
        for j in range(i + 1, len(movies)):
            if movies[i]['year'] > movies[j]['year']:
                movies[i], movies[j] = movies[j], movies[i]
    return movies
```
sort_alphabetically:
```
def remove_leading_words(title, words):
    title_words = title.split()
    while len(title_words) > 0 and title_words[0] in words:
        title_words.pop(0)
    return ' '.join(title_words)

def sort_alphabetically(movies):
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
```
