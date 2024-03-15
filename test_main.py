import pytest


# Тесты для структуры данных float

def test_float_addition():
    result = 2.5 + 3.7
    assert result == 6.2


def test_float_addition_negative():
    try:
        result = 2.5 + '3.7'
        assert result == 6.2
    except TypeError:
        pass


# Параметризованный тест для структуры данных float
@pytest.mark.parametrize(
    "input_value, expected",
    [
        (3.14, 3.14),
        (2.5, 2.5)
    ]
)
def test_float_parameterized(input_value, expected):
    assert float(input_value) == expected


# Тесты для структуры данных str

def test_str_concatenation():
    result = "Hello" + " " + "World"
    assert result == "Hello World"


# Параметризованный тест для структуры данных str
@pytest.mark.parametrize(
    "input_value, expected_length",
    [
        ("hello", 5),
        ("world", 5)
    ]
)
def test_str_parameterized(input_value, expected_length):
    assert len(input_value) == expected_length


# Тесты для структуры данных dict

def test_dict_update():
    data = {'key1': 'value1', 'key2': 'value2'}
    data.update({'key3': 'value3'})
    assert data == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


# Параметризованный тест для структуры данных dict

@pytest.mark.parametrize(
    "input_dict, key, expected_value",
    [
        ({"key1": "value1"}, "key1", "value1"),
        ({"key2": "value2"}, "key2", "value2")
    ]
)
def test_dict_parameterized(input_dict, key, expected_value):
    assert input_dict[key] == expected_value
