from typing import List

from app.films.film import Film


class Episode(Film):
    pass


class Series(Film):
    def __init__(self, title: str, episodes: List[Episode], rating: int = 0) -> None:
        Film.set_title(self, title)
        self.episodes = episodes
        self.rating = rating

    @property
    def duration(self):
        return sum((ep.duration for ep in self.episodes))

    def __len__(self) -> int:
        return len(self.episodes)
