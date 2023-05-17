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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_dialog import XDialog as XDialog_709d08fc


class XDialog2(XDialog_709d08fc):
    """
    Makes it possible to end a dialog and set a help id.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XDialog2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDialog2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XDialog2']

    def endDialog(self, Result: int) -> None:
        """
        hides the dialog and then causes XDialog.execute() to return with the given result value.
        """
        ...
    def setHelpId(self, Id: str) -> None:
        """
        sets the help id so that the standard help button action will show the appropriate help page.
        """
        ...


