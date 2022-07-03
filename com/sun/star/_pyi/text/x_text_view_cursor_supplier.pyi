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
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_text_view_cursor import XTextViewCursor as XTextViewCursor_d6aa0ce3

class XTextViewCursorSupplier(XInterface_8f010a43):
    """
    supplies access to the cursor in the view.
    
    This cursor is the same instance that is available in the user interface.

    See Also:
        `API XTextViewCursorSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextViewCursorSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XTextViewCursorSupplier']

    def getViewCursor(self) -> 'XTextViewCursor_d6aa0ce3':
        """
        """
        ...


