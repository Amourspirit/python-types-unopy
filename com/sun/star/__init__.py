# coding: utf-8
import os
from typing import TYPE_CHECKING

__version__ = '0.1.11'
__version_tmpl__ = "0.1.31"

_IGNORE_IMPORT_ERROR = os.environ.get(
    "ooouno_ignore_import_error", None) in ("True", "true", "yes")

if TYPE_CHECKING == False and _IGNORE_IMPORT_ERROR == False:
    raise ImportError
