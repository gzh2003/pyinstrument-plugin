from __future__ import annotations

from typing import Any

from deephaven.plugin.object_type import Exporter, FetchOnlyObjectType

from .pyinstrument_object import PyinstrumentReport


class PyinstrumentType(FetchOnlyObjectType):
    """Object type for PyinstrumentReport."""

    @property
    def name(self) -> str:
        return "pyinstrument.Report"

    def is_type(self, obj: Any) -> bool:
        return isinstance(obj, PyinstrumentReport)

    def to_bytes(self, exporter: Exporter, obj: PyinstrumentReport) -> bytes:
        return obj.html.encode("utf-8")
