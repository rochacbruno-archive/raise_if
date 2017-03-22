import raise_if


def testing_raise_if(value):
    """
    Value should not be None
    """
    raise_if(value is None, ValueError, 'You should pass a valid value!')
    print('{0} is success'.format(value))


def another_function():
    testing_raise_if(value=10)
    testing_raise_if(value=None)


if __name__ == '__main__':
    # testing_raise_if(value=None)
    another_function()
