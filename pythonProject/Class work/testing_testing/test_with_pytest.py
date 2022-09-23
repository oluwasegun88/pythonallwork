from .with_pytest import add
import pytest


@pytest.fixture()
def fixture_for_test():
    return 5


@pytest.fixture()
def db():
    return 5


@pytest.mark.number
def test_add(db):
    assert add(2, db) == 7
    assert add(6, 7) == 13
    assert add("hello", "world") == "hello world"
    assert 5 in (2, 3, 5, 6)


@pytest.mark.number
def test_add(fixture_for_test):
    assert add(2, fixture_for_test) == 7
    assert add(6, 7) == 13
    assert 5 in (2, 3, 5, 6)


@pytest.mark.strings
def test_add_with_strings(self):
    assert add("hello", "world") == "hello world"
