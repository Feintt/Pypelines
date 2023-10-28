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
