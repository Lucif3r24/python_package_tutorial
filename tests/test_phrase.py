from pytest import skip

from palindrome_Lucif3r24.phrase import Phrase


def test_non_palindrome():
    assert not Phrase("Apple").ispalindrome()

def test_literal_palindrome():
    assert Phrase("Racecar").ispalindrome

def test_mixed_case_palindrome():
    assert Phrase("RaceCar").ispalindrome

def test_palindrome_with_punctuation():
    assert Phrase("Madam, I'm Adam.").ispalindrome()

def test_letters():
    assert Phrase("Madam, I'm Adam.").letters_and_digits() == "MadamImAdam"

def test_letters_and_digits():
    assert Phrase("Madam, I'm Adam.").letters_and_digits() == "MadamImAdam"

def test_integer_non_palindrome():
    assert not Phrase(12345).ispalindrome()

def test_integer_palindrome():
    assert Phrase(12321).ispalindrome()