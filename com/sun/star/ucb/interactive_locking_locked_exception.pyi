# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from .interactive_locking_exception import InteractiveLockingException as InteractiveLockingException_7af31136
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class InteractiveLockingLockedException(InteractiveLockingException_7af31136):
    """
    Exception Class

    An error indicating that the resource is locked.
    
    **since**
    
        OOo 3.3

    See Also:
        `API InteractiveLockingLockedException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1InteractiveLockingLockedException.html>`_
    """

    typeName: Literal['com.sun.star.ucb.InteractiveLockingLockedException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., Url: typing.Optional[str] = ..., SelfOwned: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Url (str, optional): Url value.
            SelfOwned (bool, optional): SelfOwned value.
        """
        ...
    @property
    def SelfOwned(self) -> bool:
        """
        The owner of the lock.
        
        TRUE, the lock has been obtained by this OOo session. FALSE the lock has been obtained by another principal.
        """
        ...
    @SelfOwned.setter
    def SelfOwned(self, value: bool) -> None:
        ...

__all__ = ['InteractiveLockingLockedException']

