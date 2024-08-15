"""Tests for the main file."""

from main import despair

def test_we_are_correctly_viewing_caleb() -> None:
    """Checks that the function handles normal input as expected."""

    assert despair("Caleb") == "I'm very disappointed in you, Caleb."
