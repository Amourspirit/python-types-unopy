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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XSubmitListener(XEventListener_c7230c4a):
    """
    receives notifications about data being submitted.
    
    The submission may be canceled, so the listener has the possibility of verifying the data before submission.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XSubmitListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XSubmitListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XSubmitListener']

    def approveSubmit(self, Event: 'EventObject_a3d70b03') -> bool:
        """
        is invoked when a component is about to submit it's data.
        """
        ...


