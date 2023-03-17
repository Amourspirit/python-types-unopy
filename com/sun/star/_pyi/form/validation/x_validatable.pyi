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
# Namespace: com.sun.star.form.validation
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_validator import XValidator as XValidator_2a5c0f13

class XValidatable(XInterface_8f010a43):
    """
    specifies support for validating a component

    See Also:
        `API XValidatable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1validation_1_1XValidatable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.validation.XValidatable']

    def getValidator(self) -> 'XValidator_2a5c0f13':
        """
        retrieves the external instance which is currently used to validate the component
        """
        ...
    def setValidator(self, Validator: 'XValidator_2a5c0f13') -> None:
        """
        sets an external instance which is able to validate the component
        
        Any previously active validator will be revoked - there can be only one!

        Raises:
            com.sun.star.util.VetoException: ``VetoException``
        """
        ...


