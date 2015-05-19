from raise_if import raise_if


def test_passing_exception_object():
    """
    should acept exception instance
    """
    try:
        raise_if(not 1 == 2, Exception('1 not equals 2'))
    except Exception as e:
        assert str(e) == '1 not equals 2'


def test_passing_exception_type_and_arguments():
    try:
        raise_if(not 1 == 2, Exception, '1 not equals 2')
    except Exception as e:
        assert str(e) == '1 not equals 2'
