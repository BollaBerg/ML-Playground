"""
This file is intended to hold custom formatters, to use for logging.
"""
import logging


class CustomFormatter(logging.Formatter):
    """Custom formatter that can handle overrides.

    Does two things:
        If record has attribute `filename_override`: Override `filename`
        If record has attribute `lineno_override`: Override `lineno`

    Created primarily to make packages.logging.decorators.log_function_call to
    log correct meta data.
    """

    def format(self, record: logging.LogRecord) -> str:

        if hasattr(record, "filename_override"):
            record.filename = record.filename_override
        if hasattr(record, "lineno_override"):
            record.lineno = record.lineno_override

        return super().format(record)
