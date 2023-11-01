# Pypelines

The `pypelines` is a Python library designed to enhance the readability and structure of your code by introducing a clean, functional pipeline construction, similar to the `|>` operator found in languages like F# and Elixir. This approach allows for a more declarative style, where data transformations and validations are clear and linear, making the code easier to read, understand, and maintain.

## Vision

While the library currently provides the foundational capability to create and utilize pipelines in Python, our roadmap includes expanding its repertoire with a rich set of built-in functions. These functions will aid in various common tasks such as data validation, iteration, and connection, drawing inspiration from the functional programming paradigms in F# and Elixir.

## Key Features

- **Readability:** Simplifies your code structure by using the pipeline mechanism, making complex processes easy to follow.
- **Extendibility:** Designed to allow easy integration of custom functions in the pipeline, providing flexibility for your unique requirements.
- **Error Handling:** Captures and responds to errors within the pipeline through custom exception handling.

In future releases, we plan to introduce:

- **Built-in Validators:** Common checks for data types, formats, and content.
- **Iteration Tools:** Simplified ways to handle batch processing and data iteration within the pipeline.
- **Connection Helpers:** Utilities to facilitate easier data flow between different systems or components.

## Installation

You can add this library directly to your project using pip:

```bash
pip install git+https://github.com/Feintt/Pypelines.git@main#egg=pypelines
```

## Simplifying Logic with Pipelines

One of the primary motivations behind `pypelines` is to streamline the way you handle sequential logic checks or transformations, which are commonly represented with multiple if-statements. With the introduction of the '|' operator for chaining functions, you can reduce the complexity and depth of your code significantly.

## Pipes

`pypelines` has 3 main classes, simple, but extreamly effective.
- PipeValidator: When you need to verify data trough a pipe
- PipeModifier: For modifying data trough a pipe (the most common pipe)
- PipeExecuter: When execute some code in the middle of pipes without braking the things

# Example for PipeValidator

## Traditional aproach

Here it will be the traditional aproach

## With pypelines

aproach with pypelines

In this structure, each function represents a step in your processing pipeline. If any step fails, the `PipelineBrokenError` captures where and why, without the need for nested conditionals. This not only makes your code cleaner but also encapsulates each logic check within its function, promoting reusability and organization.

## Documentation

### Defining Pipeline Functions
To create a new function that can be included in a pipeline, use the PipeFunction decorator:
```python
from pipeline_lib import PipeFunction

@PipeFunction
def your_function_name(your_parameters):
    # Your code here
    pass
```

### Creating a Pipeline
Combine multiple functions into a pipeline using the '|' operator instead of using multiple if statements!

```python
result = your_input_data | function_one | function_two | function_three
```
