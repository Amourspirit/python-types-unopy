=======================
LibreOffice API Typings
=======================

This project allow typings for the full `LibreOffice API <https://api.libreoffice.org/>`_

WHY
===

Working with `LibreOffice API <https://api.libreoffice.org/>`_ in a modern code editor such as `Visual Studio Code <https://code.visualstudio.com/>`_
there is not type support for `LibreOffice API <https://api.libreoffice.org/>`_ This project solves that Issue.

VERSION
=======

This package is for Version ``7.4`` + of `LibreOffice API <https://api.libreoffice.org/>`_.

From one version of LibreOffice to the next, generally speaking, the API does not changed much.
Because this is the case it is very likely this current version of ``LibreOffice API Typings``
will work fine with other versions of LibreOffice. This a typing package so not much can go wrong in other versions.

Installation
============

PIP
---

**types-unopy** on `PyPI <https://pypi.org/project/types-unopy/>`_

.. code-block:: bash

    $ pip install types-unopy

For version ``7.3`` (or less) of LibreOffice.

.. code-block:: bash

    $ pip install "types-unopy<1.0"

CONDA
-----

**types-unopy** on `Anaconda <https://anaconda.org/conda-forge/types-unopy>`_

.. code-block:: bash

    $ conda install -c conda-forge types-unopy

For version ``7.3`` (or less) of LibreOffice.

.. code-block:: bash

    $ conda install -c conda-forge "types-unopy<1.0"

Related
=======

`Types-ScriptForge leverages <https://github.com/Amourspirit/python-types-scriptforge>`_ ``types-unopy``. By installing
Types-ScriptForge into your project you will also automatically install ``types-unopy``.

USAGE
=====

Not all object in `LibreOffice API <https://api.libreoffice.org/>`_ can be directly imported.

Any UNO object that is a *service* cannot be imported at runtime.

For instance if you need to import ``SheetCellRange`` so it can be used
as type the following will fail at runtime.

.. code-block:: python

    >>> from com.sun.star.sheet import SheetCellRange
    ImportError: No module named 'com' (or 'com.sun.star.sheet.SheetCellRange' is unknown)

The solution is to use `TYPE_CHECKING <https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING>`_.

.. code-block:: python

    >>> from __future__ import annotations
    >>> from typing import TYPE_CHECKING
    >>> if TYPE_CHECKING:
    ...     from com.sun.star.sheet import SheetCellRange
    ...

Anything imported in the ``TYPE_CHECKING`` block will not be available at runtime.
For this reason types inside the ``TYPE_CHECKING`` must be wrapped in quotes **OR** ``from __future__ import annotations`` must be the first line of the module.

Example of wrapping type in quotes.

.. code-block:: python

    def do_work(range: 'SheetCellRange') -> None: ...

Known Issues
============

Enums
-----

There is no enum classes in API only enum members.

To access the enum members they must be imported directly.

For example to import ``com.sun.star.beans.PropertyState.DIRECT_VALUE``


If you need the behavior of regular Enum Classes consider using `ooouno <https://github.com/Amourspirit/python-ooouno>`_

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

Demo
====

.. figure:: https://user-images.githubusercontent.com/4193389/163689461-ab349f19-81b0-450b-bf49-50303a5c4da4.gif
    :alt: Example image.

Special Cases
=============

By default an ``ImportError`` is raised when importing form ``com.sun.star`` at runtime.
This is by design as the import error triggers ``uno`` to search LibreOffice API for actual import;
Otherwise, ``com.sun.star`` is seen a namespace import and ``uno`` is ignored.

In some cases the ``ImportError`` may need to be suppressed.

Suppressing ``ImportError`` is accomplished by adding ``"ooouno_ignore_import_error"`` to environment and setting it to ``"True"``

.. code-block:: python

    >>> import os
    >>> os.environ["ooouno_ignore_import_error"] = "True" # must be string

When building with `Sphinx`_ and `autodoc`_ it may be necessary to exclude uno related imports.
This can be accomplished using the `autodoc_mock_imports <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_mock_imports>`_ option.

.. code-block:: python

    # docs conf.py
    autodoc_mock_imports = ['uno', 'unohelper', 'com']

Related Projects
================

* `OOO Development Tools <https://github.com/Amourspirit/python_ooo_dev_tools>`__
* `ooouno <https://github.com/Amourspirit/python-ooouno>`__
* `ScriptForge Typings <https://github.com/Amourspirit/python-types-scriptforge>`__
* `Access2base Typings <https://github.com/Amourspirit/python-types-access2base>`__
* `LibreOffice Python UNO Examples <https://github.com/Amourspirit/python-ooouno-ex>`__
* `LibreOffice UNO Typings <https://github.com/Amourspirit/python-types-uno-script>`__
* `LibreOffice Developer Search <https://github.com/Amourspirit/python_lo_dev_search>`__
* `OOO UNO TEMPLATE <https://github.com/Amourspirit/ooo_uno_tmpl>`__

.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html