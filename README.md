# raise_if

Python could have raise conditions like Ruby.

```ruby
def i_must_have_truth(value)
  raise TypeError, 'You must give me truth' if value == false
end
```

But the only one line option that works hurts PEP8
```python
def i_must_have_truth(value):
    if not value: raise TypeError('You must give me truth')
```

So..

```python
$ pip install raise_if

def i_must_have_truth(value):
    raise_if(not value, TypeError, 'You must give me truth')
```

Pass exception type and arguments

```python
raise_if(not 1 == 2, TypeError, 'Fails', another_arg='foo')
```

or

```python
raise_if(not 1 == 2, TypeError('Fails', another_arg='foo'))
```

Why??

Because I am lazy and I do not like extra breaks in a chain of if statements!

:)


