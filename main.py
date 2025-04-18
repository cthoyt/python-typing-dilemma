# /// script
# requires-python = ">=3.13"
# ///

from typing import Any, TypeVar, reveal_type

type Record = dict[str, Any]


class Element:
    def __init__(self, record: Record) -> None:
        self.record = record


class DerivedElement(Element):
    pass


# note, we're using PEP-696 default keyword, which is available from Python 3.13 onwards
T = TypeVar("T", bound=Element, default=Element)


def from_record_1(record: Record, element_cls: type[T] = Element) -> T:
    return element_cls(record)


REC = {"a": "b"}

reveal_type(from_record_1(REC))  # reveals Element, since this is default
reveal_type(from_record_1(REC, element_cls=Element))  # reveals Element
reveal_type(from_record_1(REC, element_cls=DerivedElement))  # reveals DerivedElement


# on a second try, I got sneaky with the type inference, but this gets a different error


def from_record_2(record: Record, element_cls: type[T] | None = None) -> T:
    if element_cls is None:
        return Element(record)
    return element_cls(record)


reveal_type(from_record_2(REC))  # reveals Element, since this is default
reveal_type(from_record_2(REC, element_cls=Element))  # reveals Element
reveal_type(from_record_2(REC, element_cls=DerivedElement))  # reveals DerivedElement
