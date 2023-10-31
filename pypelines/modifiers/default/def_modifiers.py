from pypelines.modifiers import PipeModifier
from typing import Callable, Any


@PipeModifier
def enum(x: Any, func: Callable):
    if isinstance(x, tuple):
        return func(*x)
    return func(x)
