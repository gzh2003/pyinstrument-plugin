from deephaven.plugin import Registration, Callback
from deephaven.plugin.utilities import create_js_plugin, DheSafeCallbackWrapper

from .pyinstrument_type import PyinstrumentType

PACKAGE_NAMESPACE = "deephaven.plugin.pyinstrument"
JS_NAME = "_js"


class PyinstrumentRegistration(Registration):
    @classmethod
    def register_into(cls, callback: Callback) -> None:
        callback = DheSafeCallbackWrapper(callback)
        callback.register(PyinstrumentType)

        js_plugin = create_js_plugin(PACKAGE_NAMESPACE, JS_NAME)
        callback.register(js_plugin)
