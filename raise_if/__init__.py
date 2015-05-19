"""raise_if - raise exception if condition"""

__version__ = '0.1.0'
__author__ = 'Bruno Rocha <rochacbruno@gmail.com>'
__all__ = ["raise_if"]


def raise_if(condition, exception, *args, **kwargs):
    if condition:
        raise exception if isinstance(
            exception, Exception
        ) else exception(
            *args, **kwargs
        )
