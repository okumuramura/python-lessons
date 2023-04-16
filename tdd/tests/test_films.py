import pytest
import json

from app.films.film import Film

def test_constructor():
    film = Film("Какой-то фильм", 30)
    assert film.title == "Какой-то фильм"
    assert film.duration == 30

def test_too_long_title():
    title = 't' * 101
    with pytest.raises(ValueError):
        Film(title, 10)

def test_str_method():
    film = Film("Star Bars", 239)
    assert str(film) == "Star Bars 3:59"

def test_str_method_no_hours():
    film = Film('short film', 5)
    assert str(film) == "short film 0:05"

def test_save_json(temp_file: str):
    film = Film('some film', 120, 2)
    expected = {
        'title': 'some film',
        'duration': 120,
        'rating': 2
    }
    film.save(temp_file)

    with open(temp_file, 'r', encoding='utf-8') as file:
        actual = json.load(file)

    assert expected == actual


# py -m pip install pytest
