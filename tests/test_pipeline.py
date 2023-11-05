from pypelines.validators import *
from pypelines.modifiers import *
from pypelines.executers import *

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

my_var = "hello@world.com"
result = (my_var
          | starts_with("hello")
          | is_email
          | ends_with(".com")
          | sample_data
          | max_length(15)
          | PipeModifier(str.upper)
          | contains_substring("WORLD")
          )
assert result == "HELLO@WORLD.COM", "Test4 failed"
print("Test5 passed")


@PipeModifier
def return_two_values(x):
    return x, x + 1


@PipeModifier(unpack=True)
def sum_two_values(x, y):
    return x + y


@PipeModifier
def raise_by(x, by):
    return x ** by


z = 2
result = (z
          | return_two_values
          | sum_two_values
          | raise_by(2)
          )
assert result == 25, "Test6 failed"
print("Test6 passed")


def do_something():
    return 5


result = (do_something()
          | raise_by(5)
          )
assert result == 3125, "Test7 failed"
print("Test7 passed")

my_list = [1, 2, 3, 4, 5]

if result := (my_list | sum_list | square | raise_by(2)):
    assert result == 50625, "Test8 failed"
    print("Test8 passed")


@PipeValidator(unpack=True, skip=False)
def authenticate_user(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False


(("admin", "admin") | authenticate_user() | debug_print)

my_list = "abcde"
my_list | enum(lambda x: [y for y in x]) | PipeExecute(print)
