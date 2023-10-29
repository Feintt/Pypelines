from pypelines.validators import PipeValidator, PipeValidatorBrokenError
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
        assert result == my_email
except PipeValidatorBrokenError as e:
    print(f"Validatuon error: {e}")


@PipeModifier
def square(x):
    return x * x


@PipeModifier
def sum_list(x: list):
    return sum(x)


my_list = [1, 2, 3, 4, 5]

if result := (my_list | sum_list | square):
    assert result == 225
