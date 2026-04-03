from main import sum

def test_sum():
    expected = 10
    result = sum(2, 8)

    assert(result == expected), "É esperado que o resultado seja 10"