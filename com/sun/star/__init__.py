import os
from typing import TYPE_CHECKING

__version__ = "1.2.3"
__version_tmpl__ = "0.3.6"

_IGNORE_IMPORT_ERROR = os.environ.get(
    "ooouno_ignore_import_error", None) in ("True", "true", "yes")

if TYPE_CHECKING is False and _IGNORE_IMPORT_ERROR is False:
    raise ImportError("Are you sure that uno has been imported?")
