import pytest

from app.films.series import Series, Episode

@pytest.fixture
def valid_episodes():
    return [Episode(f'ep {x}', 5) for x in range(5)]

@pytest.fixture
def valid_series(valid_episodes):
    return Series('test series', valid_episodes)

def test_constructor(valid_series: Series):
    assert valid_series.title == 'test series'


def test_series_duration(valid_series: Series):
    assert valid_series.duration == 5 * 5

    with pytest.raises(AttributeError):
        valid_series.duration = 5

def test_series_str_method(valid_series: Series):
    assert str(valid_series) == "test series 0:25"

def test_len_method(valid_series: Series):
    assert len(valid_series) == len(valid_series.episodes)
