LibreOffice API typings
=======================

This project allow typings for the full `LibreOffice API <https://api.libreoffice.org/>`_
WHY
---

Working with `LibreOffice API <https://api.libreoffice.org/>`_ in a modern IDE such as `Visual Studio Code <https://code.visualstudio.com/>`_
there is not type support for `LibreOffice API <https://api.libreoffice.org/>`_ This project solves that Issue.


USAGE
-----

Not all object in `LibreOffice API <https://api.libreoffice.org/>`_ can be directly imported.

For instance if you need to import ``SheetCellRange`` so it can be used as type the following will fail
at runtime.

.. code-block:: python

    >>> from com.sun.star.sheet import SheetCellRange
    ImportError: No module named 'com' (or 'com.sun.star.sheet.SheetCellRange' is unknown)

The solution is to use ``TYPE_CHECKING``.

.. code-block:: python

    >>> from typing import TYPE_CHECKING
    >>> if TYPE_CHECKING:
    ...     from com.sun.star.sheet import SheetCellRange
    ...
    # anything insed of TYPE_CHECKING block is ignore at runtime.

Known Issues
------------

Enums
+++++

There is no enum classes in API only enum members.

To acces the enum members they must be imported directly.

For example to import ``com.sun.star.beans.PropertyState.DIRECT_VALUE``


If you need the behaviour of regular Enum Classes consider using `ooouno <https://github.com/Amourspirit/python-ooouno>`_

.. code-block:: python

    >>> from com.sun.star.beans import PropertyState
    ImportError: No module named 'com' (or 'com.sun.star.beans.PropertyState' is unknown
    >>>
    >>> from com.sun.star.beans.PropertyState import DIRECT_VALUE
    >>> DIRECT_VALUE.value
    'DIRECT_VALUE'
    >>>
    >>> type(DIRECT_VALUE)
    <class 'uno.Enum'>
