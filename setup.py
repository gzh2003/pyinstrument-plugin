from setuptools import setup
import os
from deephaven.plugin.packaging import package_js

js_dir = "src/js/"
dest_dir = os.path.join("src/deephaven/plugin/pyinstrument/_js")

package_js(js_dir, dest_dir)

setup(package_data={"deephaven.plugin.pyinstrument._js": ["**"]})
