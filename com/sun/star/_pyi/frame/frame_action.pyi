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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class FrameAction(Enum):
    """
    Enum

    

    See Also:
        `API FrameAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame.html#a793fdb3e5cab69d63a9c89b5e4f83dfd>`_
    """
    typeName: str = 'com.sun.star.frame.FrameAction'

    COMPONENT_ATTACHED: 'uno.Enum'
    """
    an event of this kind is broadcast whenever a component is attached to a frame
    
    This is almost the same as the instantiation of the component within that frame. The component is attached to the frame immediately before this event is broadcast.
    """
    COMPONENT_DETACHING: 'uno.Enum'
    """
    an event of this kind is broadcast whenever a component is detaching from a frame
    
    This is quite the same as the destruction of the component which was in that frame. At the moment when the event is broadcast the component is still attached to the frame but in the next moment it won't.
    """
    COMPONENT_REATTACHED: 'uno.Enum'
    """
    an event of this kind is broadcast whenever a component is attached to a new model.
    
    In this case the component remains the same but operates on a new model component.
    """
    CONTEXT_CHANGED: 'uno.Enum'
    """
    an event of this kind is broadcast whenever a component changes its internal context (i.e., the selection).
    
    If the activation status within a frame changes, this counts as a context change too.
    """
    FRAME_ACTIVATED: 'uno.Enum'
    """
    an event of this kind is broadcast whenever a component gets activated
    
    Activations are broadcast from the top component which was not active before, down to the inner most component.
    """
    FRAME_DEACTIVATING: 'uno.Enum'
    """
    an event of this kind is broadcasted immediately before the component is deactivated
    
    Deactivations are broadcast from the innermost component which does not stay active up to the outer most component which does not stay active.
    """
    FRAME_UI_ACTIVATED: 'uno.Enum'
    """
    an event of this kind is broadcast by an active frame when it is getting UI control (tool control).
    """
    FRAME_UI_DEACTIVATING: 'uno.Enum'
    """
    an event of this kind is broadcast by an active frame when it is losing UI control (tool control).
    """

