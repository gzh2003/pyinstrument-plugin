from __future__ import annotations

from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable, Generator, Optional, TypeVar

from pyinstrument import Profiler  # type: ignore[attr-defined]

T = TypeVar("T")


class ProfileContext:
    """Context object that holds the profiler and resulting report."""

    def __init__(self, profiler: Profiler):
        self._profiler = profiler
        self._report: Optional[PyinstrumentReport] = None

    @property
    def profiler(self) -> Profiler:
        return self._profiler

    @property
    def report(self) -> Optional[PyinstrumentReport]:
        return self._report

    def _set_report(self, report: PyinstrumentReport) -> None:
        self._report = report


class PyinstrumentReport:
    """
    Wrapper for pyinstrument html report
    """

    def __init__(self, html_content: str):
        self._html_content = html_content

    @property
    def html(self) -> str:
        return self._html_content

    @classmethod
    def from_profiler(cls, profiler: Profiler) -> "PyinstrumentReport":
        """Create a report from a Profiler that has been started and stopped."""
        return cls(profiler.output_html())

    @classmethod
    def profile(
        cls, func: Callable[..., T], *args: Any, **kwargs: Any
    ) -> tuple[T, "PyinstrumentReport"]:
        """Profile a function call and return (result, report)."""
        profiler = Profiler()
        profiler.start()
        try:
            result = func(*args, **kwargs)
        finally:
            profiler.stop()
        return result, cls.from_profiler(profiler)

    @classmethod
    @contextmanager
    def profile_context(
        cls, interval: float = 0.001
    ) -> Generator[ProfileContext, None, None]:
        """Context manager for profiling a block of code."""
        profiler = Profiler(interval=interval)
        context = ProfileContext(profiler)
        profiler.start()
        try:
            yield context
        finally:
            profiler.stop()
            context._set_report(cls.from_profiler(profiler))


def profile(func: Callable[..., T]) -> Callable[..., tuple[T, PyinstrumentReport]]:
    """Decorator that profiles a function and returns (result, report)."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> tuple[T, PyinstrumentReport]:
        return PyinstrumentReport.profile(func, *args, **kwargs)

    return wrapper
