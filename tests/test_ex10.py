import pytest
from ppe import ex10


@pytest.mark.parametrize(
    "text, old, new, expected",
    [
        ("The fox", "fox", "dog", "The dog"),
        ("fox", "fox", "dog", "dog"),
        ("Firefox", "fox", "dog", "Firedog"),
        ("foxfox", "fox", "dog", "dogdog"),
        ("The Fox and fox.", "fox", "dog", "The Fox and dog."),
    ],
)
def test_find_and_replace(text, old, new, expected):
    assert ex10.find_and_replace(text, old, new) == expected
