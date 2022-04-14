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
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .database_parameter_event import DatabaseParameterEvent as DatabaseParameterEvent_373f0f74

class XDatabaseParameterListener(XEventListener_c7230c4a):
    """
    allows to intercept value request for parametrized SQL statements.

    See Also:
        `API XDatabaseParameterListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XDatabaseParameterListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XDatabaseParameterListener']

    def approveParameter(self, aEvent: 'DatabaseParameterEvent_373f0f74') -> bool:
        """
        is invoked when there is a need for parameter values
        """

__all__ = ['XDatabaseParameterListener']

