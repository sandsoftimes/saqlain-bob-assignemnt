from main_code import reverse_list, count_items

# Unit Testing
def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list(["apple", "orange", "banana"]) == ["banana", "orange", "apple"]

def test_count_items():
    assert count_items([1, 1, 2, 3, 3, 3]) == {1: 2, 2: 1, 3: 3}
    assert count_items(["apple", "banana", "apple", "orange", "banana"]) == {"apple": 2, "banana": 2, "orange": 1}

def test_boundary_values():
    assert reverse_list([]) == []
    assert reverse_list([1]) == [1]

def test_random_values():
    import random
    random_integers = [random.randint(1, 10) for _ in range(10)]
    assert reverse_list(reverse_list(random_integers)) == random_integers

# Run all tests
def run_tests():
    test_reverse_list()
    test_count_items()
    test_boundary_values()
    test_random_values()
    print("All tests passed!")

# Run the tests
run_tests()

