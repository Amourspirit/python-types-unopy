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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_command_processor import XCommandProcessor as XCommandProcessor_dfe80d19
    from .x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78

class XRecycler(XInterface_8f010a43):
    """
    Allows an XContent to delete itself into the trash can.
    
    This is an additional interface the XContent representing the trash can (URL: \"vnd.sun.staroffice.trashcan:///\") should support.

    See Also:
        `API XRecycler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XRecycler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XRecycler']

    def trashContent(self, Properties: 'XCommandProcessor_dfe80d19', Identifier: 'XContentIdentifier_edc90d78') -> None:
        """
        Notify the trash can that an XContent is deleting itself into it.
        """

__all__ = ['XRecycler']

