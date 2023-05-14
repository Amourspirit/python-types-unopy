# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_info_printer import XInfoPrinter as XInfoPrinter_a3fd0b1c
    from .x_printer import XPrinter as XPrinter_7ad00990

class XPrinterServer(XInterface_8f010a43):
    """
    manages several printers on one machine.

    See Also:
        `API XPrinterServer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XPrinterServer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XPrinterServer']

    def createInfoPrinter(self, printerName: str) -> 'XInfoPrinter_a3fd0b1c':
        """
        creates a new information printer.
        
        You can get all information from this printer, but the printer cannot really print.
        """
        ...
    def createPrinter(self, printerName: str) -> 'XPrinter_7ad00990':
        """
        creates a new virtual printer.
        
        You must call com.sun.star.awt.XPrinter.start() to put the job into the printer spooler.
        """
        ...
    def getPrinterNames(self) -> 'typing.Tuple[str, ...]':
        """
        returns a list of all available printer names.
        """
        ...


