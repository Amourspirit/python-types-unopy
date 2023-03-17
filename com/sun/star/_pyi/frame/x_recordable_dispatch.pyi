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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_dispatch_recorder import XDispatchRecorder as XDispatchRecorder_fbd70dd1
    from ..util.url import URL as URL_57ad07b9

class XRecordableDispatch(XInterface_8f010a43):
    """
    extends an existing XDispatch implementation with functionality for dispatch recording
    
    This interface can be implemented as an additional one beside an existing XDispatch one to provide record functionality of dispatches. Because it's an additional interface the status events are available there and not at this interface.
    
    But normally this interface mustn't be used directly. If a dispatch object is well known and recording was enabled on a XDispatchRecorderSupplier it's possible to use method XDispatchRecorderSupplier.dispatchAndRecord() of it to make dispatch and recording automatically. The interface XRecordableDispatch is used transparently there.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XRecordableDispatch <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XRecordableDispatch.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XRecordableDispatch']

    def dispatchAndRecord(self, URL: 'URL_57ad07b9', Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]', Recorder: 'XDispatchRecorder_fbd70dd1') -> None:
        """
        dispatch and record it
        """
        ...


