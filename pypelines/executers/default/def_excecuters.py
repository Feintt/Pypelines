import inspect
import logging
import random
import time

from pypelines.executers import PipeExecute


class ValidationError(Exception):
    pass


@PipeExecute
def log_data(data, level='info'):
    logger = logging.getLogger('pipeline')
    getattr(logger, level)(data)


@PipeExecute
def debug_print(data):
    # Get the calling frame and information
    frame_info = inspect.stack()[1]
    print(f"Debug print called from {frame_info.filename} at line {frame_info.lineno}: {data}")


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
