import logging
import random
import time
import traceback

from pypelines.executers import PipeExecute


class ValidationError(Exception):
    pass


@PipeExecute
def log_data(data, level='info'):
    logger = logging.getLogger('pipeline')
    getattr(logger, level)(data)


@PipeExecute
def debug_print(data):
    # Retrieve the current stack trace
    stack = traceback.extract_stack()

    # Find the stack frame outside the pypelines package
    caller_frame = next(
        (frame for frame in reversed(stack) if 'pypelines' not in frame.filename),
        None
    )

    # If a caller frame was found, print its details
    if caller_frame:
        print(f"Debug print called from {caller_frame.filename} at line {caller_frame.lineno}: \nData: {data}")
    else:
        print("Caller frame not found.")


@PipeExecute
def performance_monitor(data):
    current_time = time.time()
    print(f"Data {data} passed through at {current_time}")


@PipeExecute
def validate_data(data, schema):
    # Assume 'schema' is some form of data definition to validate against
    if not schema.is_valid(data):
        raise ValidationError(f"Data {data} failed validation")
    print(f"Data {data} passed validation")


@PipeExecute
def sample_data(data, sampling_rate=0.1):
    if random.random() < sampling_rate:
        print(f"Sampled data: {data}")  # or save to a file or database
