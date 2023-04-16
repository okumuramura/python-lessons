import json


class Film:
    def __init__(self, title: str, duration_min: int, rating: int = 0) -> None:
        self.set_title(title)
        self.duration = duration_min
        self.rating = rating

    def set_title(self, title: str) -> None:
        if len(title) > 100:
            raise ValueError('film title too long')
        self.title = title

    def __str__(self) -> str:
        duration = f'{self.duration // 60}:{self.duration % 60:02}'
        return f'{self.title} {duration}'

    def save(self, output: str) -> None:
        schema = {
            'title': self.title,
            'duration': self.duration,
            'rating': self.rating
        }

        with open(output, 'w', encoding='utf-8') as file:
            json.dump(schema, file)
