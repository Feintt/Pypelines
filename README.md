# Python Pipeline Library: `pipeline-lib`

The `pipeline-lib` is a Python library designed to enhance the readability and structure of your code by introducing a clean, functional pipeline construction, similar to the `|>` operator found in languages like F# and Elixir. This approach allows for a more declarative style, where data transformations and validations are clear and linear, making the code easier to read, understand, and maintain.

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
pip install git+https://github.com/your-username/pipeline-lib.git@main#egg=pipeline-lib
```

## Quick Start
After installing the library, you can use it in your Python scripts. Here's a simple example:

```python
from pipeline_lib import PipeFunction, PipelineBrokenError

# Define your functions using the PipeFunction decorator
@PipeFunction
def check_length(data, min_length=10):
    """Check if the data meets the minimum length requirement."""
    return len(data) >= min_length

@PipeFunction
def check_content(data):
    """Validate the content of the data."""
    # Replace with your validation logic
    return "invalid" not in data

# Create a pipeline with your functions
try:
    result = "your input data" | check_length | check_content
    print("Data passed the pipeline checks:", result)
except PipelineBrokenError as e:
    print(f"Error in pipeline processing: {e}")

```

## Simplifying Logic with Pipelines

One of the primary motivations behind `pipeline-lib` is to streamline the way you handle sequential logic checks or transformations, which are commonly represented with multiple if-statements. With the introduction of the '|' operator for chaining functions, you can reduce the complexity and depth of your code significantly.

### Traditional Approach:

In traditional code, you might find yourself dealing with nested or sequential if-statements, like so:

```python
data = "Some input"

if check_condition_one(data):
    if check_condition_two(data):
        if check_condition_three(data):
            # ...and so on...
            result = process_final(data)
        else:
            handle_error("Condition three failed.")
    else:
        handle_error("Condition two failed.")
else:
    handle_error("Condition one failed.")
```
This approach increases the complexity of your code, making it harder to read and maintain, especially as more conditions or steps are added.

## With pipeline-lib:
Our library allows you to simplify this structure drastically. The same logic can be represented linearly, reducing the cognitive load required to understand the flow:
```python
from pipeline_lib import PipeFunction, PipelineBrokenError

@PipeFunction
def check_condition_one(data):
    # Your logic here
    return "expected_result" in data

@PipeFunction
def check_condition_two(data):
    # Your logic here
    return "another_expectation" in data

# ... additional conditions ...

try:
    result = data | check_condition_one | check_condition_two | ... | process_final
    print("All conditions passed successfully:", result)
except PipelineBrokenError as e:
    print(f"A condition failed: {e}")
```

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
