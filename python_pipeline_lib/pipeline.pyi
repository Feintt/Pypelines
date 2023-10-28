from typing import Any, Callable, Type


class PipelineBrokenError(Exception):
    """Exception raised when a pipeline function fails."""
    ...


class PipeFunction:
    """Class used to create functions that can be pipelined using the '|' operator."""

    func: Callable[..., Any]

    def __init__(self, func: Callable[..., Any]) -> None: ...

    def __ror__(self, other: Callable[..., Any]) -> Callable[..., Any]: ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
