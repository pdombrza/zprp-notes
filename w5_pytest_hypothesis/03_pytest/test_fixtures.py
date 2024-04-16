from dataclasses import dataclass
import pytest
import tempfile


@dataclass
class User:
    name: str
    age: int

    @property
    def nickname(self):
        return f"{self.name.lower()}{self.age}"


# Dla uproszczenia testy w tym samym pliku


@pytest.fixture
def user_instance():
    return User("John", 42)


def test_user_nickname_typical(user_instance):
    assert user_instance.nickname == "john42"


@pytest.fixture
def setup_teardown():
    print("setup")
    yield
    print("teardown")


@pytest.fixture
def temporary_dir():  # juz istnieje ale na testa piszemy fixture co tworzy tymczasowy katalog
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


def test_naive_tmp_dir(temporary_dir):
    print(temporary_dir)
    # some actual test logic goes here


def test_with_setup_teardown(setup_teardown):
    print("in test")


@pytest.mark.slow
def test_answer_to_life(answer_to_life):
    assert answer_to_life == 42
