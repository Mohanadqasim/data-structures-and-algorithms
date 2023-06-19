import pytest
from Comparisons import sort_by_year,sort_alphabetically

def test_sort_by_year():
    movies = [
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "Pulp Fiction", "year": 1994, "genres": ["Crime", "Drama"]},
        {"title": "A Clockwork Orange", "year": 1971, "genres": ["Crime", "Drama", "Sci-Fi"]},
        {"title": "Annie Hall", "year": 1977, "genres": ["Comedy", "Romance"]},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"]},
    ]
    actual = sort_by_year(movies)
    excepted = [
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "Pulp Fiction", "year": 1994, "genres": ["Crime", "Drama"]},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"]},
        {"title": "Annie Hall", "year": 1977, "genres": ["Comedy", "Romance"]},
        {"title": "A Clockwork Orange", "year": 1971, "genres": ["Crime", "Drama", "Sci-Fi"]},
    ]
    assert actual == excepted

def test_sort_alphabetically():
    movies = [
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "Pulp Fiction", "year": 1994, "genres": ["Crime", "Drama"]},
        {"title": "A Clockwork Orange", "year": 1971, "genres": ["Crime", "Drama", "Sci-Fi"]},
        {"title": "Annie Hall", "year": 1977, "genres": ["Comedy", "Romance"]},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"]},
    ]
    actual = sort_alphabetically(movies)
    excepted = [
        {"title": "A Clockwork Orange", "year": 1971, "genres": ["Crime", "Drama", "Sci-Fi"]},
        {"title": "Annie Hall", "year": 1977, "genres": ["Comedy", "Romance"]},
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "Pulp Fiction", "year": 1994, "genres": ["Crime", "Drama"]},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"]},
    ]
    assert actual == excepted