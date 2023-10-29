from pypelines.validators import PipeValidator, PipeValidatorError
from pypelines.validators.default import (
    is_email,
    starts_with,
    ends_with,
    max_length,
    contains_substring
)
from pypelines.modifiers import PipeModifier

try:

    @PipeValidator
    def is_string(x):
        return isinstance(x, str)


    @PipeValidator
    def contains_at(x):
        return "@" in x


    my_email = "example@gmail.com"

    if result := (my_email | is_string | contains_at):
        assert result == my_email, "Test1 failed"
        print("Test1 passed")

    if result := (my_email | is_string | is_email):
        assert result == my_email, "Test1 failed"
        print("Test2 passed")


except PipeValidatorError as e:
    print(f"Validation error: {e}")


@PipeModifier
def square(x):
    return x * x


@PipeModifier
def sum_list(x: list):
    return sum(x)


my_list = [1, 2, 3, 4, 5]

if result := (my_list | sum_list | square):
    assert result == 225, "Test3 failed"
    print("Test3 passed")

my_var = "hello@world.com"
result = (my_var
          | starts_with("hello")
          | is_email
          | ends_with(".com")
          | max_length(15)
          | PipeModifier(str.upper)
          | contains_substring("WORLD")
          )
assert result == "HELLO@WORLD.COM", "Test4 failed"
print("Test4 passed")
