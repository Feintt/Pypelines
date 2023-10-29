from pypelines import (
    PipeValidator,
    PipeValidatorBrokenError
)

try:

    @PipeValidator
    def is_string(x):
        return isinstance(x, str)


    @PipeValidator
    def contains_at(x):
        return "@" in x


    my_email = "example@gmail.com"

    if result := (my_email | is_string | contains_at):
        pass
except PipeValidatorBrokenError as e:
    print(f"Validatuon error: {e}")
