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
# Namespace: com.sun.star.form.runtime
# Libre Office Version: 7.2
from typing_extensions import Literal
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class FilterEvent(EventObject_a3d70b03):
    """
    Struct Class

    is an event fired by a filter controller, when the filter managed by the controller changes.
    
    **since**
    
        OOo 3.3

    See Also:
        `API FilterEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1form_1_1runtime_1_1FilterEvent.html>`_
    """
    typeName: Literal['com.sun.star.form.runtime.FilterEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., DisjunctiveTerm: typing.Optional[int] = ..., FilterComponent: typing.Optional[int] = ..., PredicateExpression: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            DisjunctiveTerm (int, optional): DisjunctiveTerm value.
            FilterComponent (int, optional): FilterComponent value.
            PredicateExpression (str, optional): PredicateExpression value.
        """


    @property
    def DisjunctiveTerm(self) -> int:
        """
        denotes the index of the disjunctive term to which the event applies, if any.
        """


    @property
    def FilterComponent(self) -> int:
        """
        denotes the index of the filter component to which the event applies, if any.
        """


    @property
    def PredicateExpression(self) -> str:
        """
        denotes the predicate expression associated with the event.
        """



__all__ = ['FilterEvent']
