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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class RowChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    indicates the type of change action on the data source.

    See Also:
        `API RowChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1RowChangeEvent.html>`_
    """
    typeName: Literal['com.sun.star.sdb.RowChangeEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Action: typing.Optional[int] = ..., Rows: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Action (int, optional): Action value.
            Rows (int, optional): Rows value.
        """


    @property
    def Action(self) -> int:
        """
        indicates the type of change.
        """


    @property
    def Rows(self) -> int:
        """
        indicates the number of rows affected by the change.
        """



__all__ = ['RowChangeEvent']
