from pypelines.modifiers import PipeModifier
from typing import Callable, Any


@PipeModifier
def enum(x: Any, func: Callable):
    return func(x)
