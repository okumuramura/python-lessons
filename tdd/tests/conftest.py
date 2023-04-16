import pytest
import time
import os

@pytest.fixture
def temp_file():
    name = str(hash(time.time()))
    path = f'./{name}'
    file = open(path, 'w', encoding='utf-8')
    file.close()

    yield path

    os.remove(path)
