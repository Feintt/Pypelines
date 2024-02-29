from pypelines import Pipeable


def test_func(_data):
    return "change", {"key3": "value3"}


def test_func2(_data, changeset):
    return "change", {"key4": "value4"}


dictionary = {
    "key1": "value1",
    "key2": "value2"
}

result = Pipeable(dictionary) | test_func | test_func2
print(result.get_changeset())
