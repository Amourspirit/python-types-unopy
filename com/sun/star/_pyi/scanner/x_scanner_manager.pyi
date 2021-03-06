# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.3
# Namespace: com.sun.star.scanner
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.x_bitmap import XBitmap as XBitmap_70cd0909
    from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
    from .scan_error import ScanError as ScanError_b0d90b81
    from .scanner_context import ScannerContext as ScannerContext_f0c60da1

class XScannerManager(XInterface_8f010a43):
    """

    See Also:
        `API XScannerManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1scanner_1_1XScannerManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.scanner.XScannerManager']

    def configureScanner(self, scannerContext: object) -> bool:
        """
        produce some kind of User Interface to let the user have a preview, configure the scan area, etc., it returns FALSE if user cancelled this process

        Raises:
            com.sun.star.scanner.ScannerException: ``ScannerException``
        """
        ...
    def getAvailableScanners(self) -> 'typing.Tuple[ScannerContext_f0c60da1, ...]':
        """
        returns all available scanner devices
        """
        ...
    def getBitmap(self, scannerContext: 'ScannerContext_f0c60da1') -> 'XBitmap_70cd0909':
        """
        get the image after completion of scan

        Raises:
            com.sun.star.scanner.ScannerException: ``ScannerException``
        """
        ...
    def getError(self, scannerContext: 'ScannerContext_f0c60da1') -> 'ScanError_b0d90b81':
        """
        get the state of scanning after completion of scan

        Raises:
            com.sun.star.scanner.ScannerException: ``ScannerException``
        """
        ...
    def startScan(self, scannerContext: 'ScannerContext_f0c60da1', listener: 'XEventListener_c7230c4a') -> None:
        """
        start the scanning process listener will be called when scan is complete the EventObject of the disposing call will contain the ScannerManager if the scan was successful, an empty interface otherwise

        Raises:
            com.sun.star.scanner.ScannerException: ``ScannerException``
        """
        ...


