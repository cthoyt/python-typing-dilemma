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


def from_record(record: Record, element_cls: type[T] = Element) -> T:
    return element_cls(record)


REC = {"a": "b"}

reveal_type(from_record(REC))  # reveals Element, since this is default
reveal_type(from_record(REC, element_cls=Element))  # reveals Element
reveal_type(from_record(REC, element_cls=DerivedElement))  # reveals DerivedElement
