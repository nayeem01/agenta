# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .span import Span
from .span_kind import SpanKind
from .span_status_code import SpanStatusCode
from .span_variant import SpanVariant

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SpanDetail(pydantic.BaseModel):
    id: str
    name: str
    parent_span_id: typing.Optional[str]
    created_at: dt.datetime
    variant: SpanVariant
    environment: typing.Optional[str]
    spankind: SpanKind
    status: SpanStatusCode
    metadata: typing.Dict[str, typing.Any]
    user_id: typing.Optional[str]
    children: typing.Optional[typing.List[Span]]
    content: typing.Dict[str, typing.Any]
    config: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
