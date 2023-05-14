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
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_database_parameter_listener import XDatabaseParameterListener as XDatabaseParameterListener_77e01110

class XDatabaseParameterBroadcaster(XInterface_8f010a43):
    """
    provides the possibility of receiving an event for configuration of parameters.
    
    This interface is usually implemented by components which are to execute a statement, and may need parameter information. For example, the com.sun.star.form.component.DataForm is such a component. When it is bound to a statement which contains parameters, or to a query which is based upon a parametrized statement, it needs values to fill in the parameters with actual values when it is being loaded. One method to gather these values is calling the XDatabaseParameterListener listeners, which can fill them in.

    See Also:
        `API XDatabaseParameterBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XDatabaseParameterBroadcaster.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XDatabaseParameterBroadcaster']

    def addParameterListener(self, aListener: 'XDatabaseParameterListener_77e01110') -> None:
        """
        adds the specified listener, to allow it to fill in necessary parameter values.
        """
        ...
    def removeParameterListener(self, aListener: 'XDatabaseParameterListener_77e01110') -> None:
        """
        removes the specified listener.
        """
        ...


