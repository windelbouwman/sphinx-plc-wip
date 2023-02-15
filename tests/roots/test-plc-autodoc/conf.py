import os
import sys

sys.path.insert(0, os.path.abspath("."))

extensions = ["sphinx.ext.autodoc", "plcdoc"]

# The suffix of source filenames.
source_suffix = ".rst"

nitpicky = True

plc_sources = [os.path.join(os.path.abspath("."), "src_plc/*.TcPOU")]
