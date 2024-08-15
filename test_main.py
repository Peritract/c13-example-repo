"""Tests for the main file."""

from main import assess

def test_we_are_correctly_viewing_caleb() -> None:
    """Checks that the function handles normal input as expected."""

    assert assess("Caleb") == "I could never be disappointed in you, Caleb."
