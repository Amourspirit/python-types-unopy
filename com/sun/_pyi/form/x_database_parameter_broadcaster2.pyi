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
from .x_database_parameter_broadcaster import XDatabaseParameterBroadcaster as XDatabaseParameterBroadcaster_ac7f1234
if typing.TYPE_CHECKING:
    from .x_database_parameter_listener import XDatabaseParameterListener as XDatabaseParameterListener_77e01110

class XDatabaseParameterBroadcaster2(XDatabaseParameterBroadcaster_ac7f1234):
    """
    provides the possibility of receiving an event for configuration of parameters.
    
    Note that this interface provides exactly the same functionality as the XDatabaseParameterBroadcaster interface. It exists purely for compatibility with the com.sun.star.script.XEventAttacher.attachSingleEventListener(): It expects the methods for adding and removing listeners to follow a certain naming scheme, respective to the name of the listener which is being added/removed.

    See Also:
        `API XDatabaseParameterBroadcaster2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XDatabaseParameterBroadcaster2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XDatabaseParameterBroadcaster2']

    def addDatabaseParameterListener(self, aListener: 'XDatabaseParameterListener_77e01110') -> None:
        """
        registers an XDatabaseParameterListener
        
        This method behaves exactly as the XDatabaseParameterBroadcaster.addParameterListener() method inherited from the base interface.
        """
    def removeDatabaseParameterListener(self, aListener: 'XDatabaseParameterListener_77e01110') -> None:
        """
        revokes an XDatabaseParameterListener
        
        This method behaves exactly as the XDatabaseParameterBroadcaster.removeParameterListener() method inherited from the base interface.
        """

__all__ = ['XDatabaseParameterBroadcaster2']

