import raise_if


def test_passing_exception_object():
    """
    should acept exception instance
    """
    try:
        raise_if(not 1 == 2, Exception('1 not equals 2'))
    except Exception as e:
        assert '1 not equals 2' in str(e)
        assert 'tests.py' in str(e)
        assert 'test_passing_exception_object' in str(e)
        assert 'line: 9' in str(e)


def test_passing_exception_type_and_arguments():
    """
    should accept Exception type and arguments
    """
    try:
        raise_if(not 1 == 2, ValueError, '1 not equals 2')
    except ValueError as e:
        assert '1 not equals 2' in str(e)
        assert 'tests.py' in str(e)
        assert 'test_passing_exception_type_and_arguments' in str(e)
        assert 'line: 22' in str(e)
