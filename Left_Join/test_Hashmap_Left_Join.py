import pytest
from Hashmap_Left_Join import left_join

def test_left_join_basic():
    synonyms = {
        'happy': 'joyful',
        'sad': 'unhappy',
        'big': 'large'
    }

    antonyms = {
        'happy': 'sad',
        'sad': 'happy',
        'big': 'small'
    }

    result = left_join(synonyms, antonyms)
    expected_result = {
        'happy': ('joyful', 'sad'),
        'sad': ('unhappy', 'happy'),
        'big': ('large', 'small')
    }
    assert result == expected_result


def test_left_join_missing_antonyms():
    synonyms = {
        'happy': 'joyful',
        'sad': 'unhappy',
        'big': 'large'
    }

    antonyms = {}

    result = left_join(synonyms, antonyms)
    expected_result = {
        'happy': ('joyful', None),
        'sad': ('unhappy', None),
        'big': ('large', None)
    }
    assert result == expected_result

def test_left_join_missing_synonyms():
    synonyms = {}

    antonyms = {
        'happy': 'sad',
        'sad': 'happy',
        'big': 'small'
    }

    result = left_join(synonyms, antonyms)
    expected_result = {}
    assert result == expected_result

def test_left_join_mixed_scenario():
    synonyms = {
        'happy': 'joyful',
        'sad': 'unhappy',
        'big': 'large',
        'small': 'tiny'
    }

    antonyms = {
        'happy': 'sad',
        'big': 'small',
        'fast': 'slow'
    }

    result = left_join(synonyms, antonyms)
    expected_result = {
        'happy': ('joyful', 'sad'),
        'sad': ('unhappy', None),
        'big': ('large', 'small'),
        'small': ('tiny', None)
    }
    assert result == expected_result

def test_left_join_empty_input():
    synonyms = {}
    antonyms = {}

    result = left_join(synonyms, antonyms)
    expected_result = {}
    assert result == expected_result

pytest.main()
