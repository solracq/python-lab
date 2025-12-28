import pytest
from string_calculator import StringCalculator

"""
add("") → 0.
add("1") → 1.
add("1,2") → 3.
add("1,2,3,4") → 10.
add("1\n2,3") → 6 (support newline as delimiter).
add("//;\n1;2") → 3 (support custom single-char delimiter syntax //[delim]\n).
add("1,-2,3") → throw IllegalArgumentException listing negatives.
Numbers > 1000 are ignored: add("2,1001") → 2.
Optional: allow multi-char delimiters like //[***]\n1***2***3.
"""
@pytest.fixture
def calculator():
    return StringCalculator()

def test_empty_string_return_zero(calculator):
    assert calculator.add("") == 0

def test_single_number_returns_its_value(calculator):
    assert calculator.add("1") == 1

def test_two_numbers_are_summed(calculator):
    assert calculator.add("1, 2") == 3

def test_multiple_numbers_are_summed(calculator):
    assert calculator.add("1, 2, 3, 4") == 10

@pytest.mark.parametrize("numbers, expected", [
    ("5", "5")
])
def test_multiple_parametrize(calculator, numbers, expected):
    assert calculator.add(numbers) == expected, "Wrong output"

def test_newline_delimiter_is_supported(calculator):
    assert calculator.add("1\n2,3") == 6

def test_custom_delimiter_single_char(calculator):
    assert calculator.add("//;\n1;2") == 3, f"Issue Found!"

def test_negative_numbers_rise_exception(calculator):
    with pytest.raises(ValueError) as execinfo:
        calculator.add("1,-2,3")
    assert "negatives not allowed -2" in str(execinfo.value)

def test_numbers_grater_than_1000_are_ignored(calculator):
    assert calculator.add("2,1001") == 2

@pytest.mark.parametrize("a, b, expected", [(5, 2, 7), (1, 2, 3), (7, 8, 15)])
def test_sum(calculator, a, b, expected):
    assert a + b == expected

##################################################
def sample_data():
    return [1, 2, 3]

@pytest.mark.parametrize("input", sample_data())
def test_input_data(input):
    assert input in [1, 2, 3]

####################################################
@pytest.fixture
def sample_data(request):
    return request.param

@pytest.mark.parametrize("sample_data", [1, 2, 3], indirect=True)
def test_input_req_param(sample_data):
    assert sample_data in [1, 2, 3]
