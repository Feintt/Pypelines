from pypelines.modifiers import PipeModifier


@PipeModifier
def enum_list(x: list):
    return enumerate(x)