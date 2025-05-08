import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("tomato", "Tomato"),
    ("hello world", "Hello world"),
    ("pytest", "Pytest"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Tomato", "Tomato"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, ret", [
    ("SkyPro", "S", True),
    ])
def test_contains_positive(string, symbol, ret):
    assert string_utils.contains(string, symbol) == ret


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, ret", [
    ("SkyPro", "T", False),
])
def test_contains_negative(string, symbol, ret):
    assert string_utils.contains(string, symbol) == ret


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, ret", [
    ("SkyPro", "Pro", "Sky" ),
    ])
def test_delete_symbol_positive(string, symbol, ret):
    assert string_utils.delete_symbol(string, symbol) == ret


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, ret", [
    ("", "", "" ),
    ])
def test_delete_symbol_negative(string, symbol, ret):
    assert string_utils.delete_symbol(string, symbol) == ret