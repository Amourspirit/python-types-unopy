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
# Namespace: com.sun.star.document
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
from ..frame.x_model import XModel as XModel_7a6e095c

class FilterOptionsRequest(Exception_85530a09):
    """
    Exception Class

    Is used for interaction handle to get filter options.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API FilterOptionsRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1document_1_1FilterOptionsRequest.html>`_
    """

    typeName: Literal['com.sun.star.document.FilterOptionsRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., rModel: typing.Optional[XModel_7a6e095c] = ..., rProperties: typing.Optional[typing.Tuple[PropertyValue_c9610c73, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            rModel (XModel, optional): rModel value.
            rProperties (typing.Tuple[PropertyValue, ...], optional): rProperties value.
        """
        ...
    @property
    def rModel(self) -> XModel_7a6e095c:
        """
        The model of the document that should be provided to filters that supports XExporter interface.
        """
        ...
    @rModel.setter
    def rModel(self, value: XModel_7a6e095c) -> None:
        ...
    @property
    def rProperties(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        The Media-descriptor of the document.
        """
        ...
    @rProperties.setter
    def rProperties(self, value: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        ...

__all__ = ['FilterOptionsRequest']

