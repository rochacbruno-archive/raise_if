"""raise_if - raise exception if condition"""
import sys

__version__ = '0.1.4'
__author__ = 'Bruno Rocha <rochacbruno@gmail.com>'
__all__ = ["raise_if"]


def raise_if(condition, exception, *args, **kwargs):
    if condition:
        # import inspect here because of pytest/nose circular imports
        import inspect  # noqa

        frame_info = inspect.stack()[1]
        parent_frame_info = inspect.stack()[2]

        exp = exception if isinstance(
            exception, Exception
        ) else exception(
            *args, **kwargs
        )

        new_message = str(exp)
        new_message += (
            u'\n ---- details ----\n'
            u'filename: {1}\n'
            u'line: {2}\n'
            u'caller name: {3}\n'
        ).format(*frame_info)
        new_message += (
            u'\n'
            u'filename: {1}\n'
            u'line: {2}\n'
            u'parent caller name: {3}\n'
        ).format(*parent_frame_info)

        raise exp.__class__(new_message)


sys.modules[__name__] = raise_if
