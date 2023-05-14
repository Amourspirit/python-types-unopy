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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt.tree
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ...util.veto_exception import VetoException as VetoException_bdad0c13
from ...uno.x_interface import XInterface as XInterface_8f010a43
from .tree_expansion_event import TreeExpansionEvent as TreeExpansionEvent_378b0f79

class ExpandVetoException(VetoException_bdad0c13):
    """
    Exception Class

    Exception used to stop an expand/collapse from happening.

    See Also:
        `API ExpandVetoException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1awt_1_1tree_1_1ExpandVetoException.html>`_
    """

    typeName: Literal['com.sun.star.awt.tree.ExpandVetoException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Event: typing.Optional[TreeExpansionEvent_378b0f79] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Event (TreeExpansionEvent, optional): Event value.
        """
        ...
    @property
    def Event(self) -> TreeExpansionEvent_378b0f79:
        """
        The event that the exception was created for.
        """
        ...
    @Event.setter
    def Event(self, value: TreeExpansionEvent_378b0f79) -> None:
        ...

__all__ = ['ExpandVetoException']

