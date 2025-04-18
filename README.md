# python-typing-dilemma

This repository wraps an issue I've had with writing correct types when using
[PEP-696](https://peps.python.org/pep-0696/) defaults in `typing.TypeVar`.

The goal is to have a function `from_record()` that knows to make a base class
by default, but also allows for passing derived classes from the base class.

It should know if you pass a class to `element_cls`, to dispatch to creating
that class and then should be smart enough to narrow the return type. If no
`element_cls` is returned, then it shouldn't narrow the return type, and instead
just use the default.

```python
REC = {"a": "B"}
typing.reveal_type(from_record(REC))  # reveals Element, since this is default
typing.reveal_type(from_record(REC, element_cls=Element))  # reveals Element
typing.reveal_type(from_record(REC, element_cls=DerivedElement))  # reveals DerivedElement
```

The problem, is how to type `element_cls`? I am writing this because I hope
someone can help! I have tried using variations on how `T` is defined, defining
other variants of `T` that include `type[Element]` inside, and using overloads,
but nothing worked so far.

The example can be found in [`main.py`](main.py), and reproduced with MyPy (on
Python 3.13+, because of when PEP-696 was added to stdlib) with the following
commands:

```console
$ git clone https://github.com/cthoyt/python-typing-dilemma
$ cd python-typing-dilemma
$ uvx --python 3.13 mypy --strict main.py
main.py:23: error: Incompatible default for argument "element_cls" (default has type "type[Element]", argument has type "type[T]")  [assignment]
main.py:29: note: Revealed type is "main.Element"
main.py:30: note: Revealed type is "main.Element"
main.py:31: note: Revealed type is "main.DerivedElement"
```

^ I omitted the MyPy output from the second attempt I made. If you get as far as
reproducing it, you'll see a totally different error type.

## License

MIT License
