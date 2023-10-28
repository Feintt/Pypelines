# Pipeline Library for Python

`pipeline-lib` is a Python library that enables users to create a sequence of data processing steps, each represented by a function. Functions in a pipeline are connected using the '|' operator, allowing for clear and concise data flow. This library is particularly useful for data validation, transformation, and more.

## Features

- Easy-to-use pipeline creation using the '|' operator.
- Customizable validation or processing functions.
- Exception handling to capture and respond to errors in the pipeline.

## Installation

To install `pipeline-lib`, you can add this library directly to your project using pip:

```bash
pip install git+https://github.com/Feintt/python-pipeline.git@main#egg=pipeline-lib
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
