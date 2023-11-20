import pytest

def calculate_square(x):
    return x * x

@pytest.fixture
def setup_data():
    data = 5
    print("\nSetting up resources...")
    yield data
    print("\nTearing down resources...")

def test_square_positive_number(setup_data):
    result = calculate_square(setup_data)
    assert result == 25
    print("Running test case for positive number")

def test_square_negative_number(setup_data):
    result = calculate_square(-setup_data)
    assert result == 25
    print("Running test case for negative number")
