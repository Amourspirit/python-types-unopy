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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.text.textfield
import typing
from ..text_field import TextField as TextField_90260a56
if typing.TYPE_CHECKING:
    from ...util.date import Date as Date_60040844
    from ...util.date_time import DateTime as DateTime_84de09d3

class Annotation(TextField_90260a56):
    """
    Service Class

    specifies service of an annotation text field.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API Annotation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1Annotation.html>`_
    """
    @property
    def Author(self) -> str:
        """
        contains the name of the author of the annotation.
        """
        ...
    @property
    def Content(self) -> str:
        """
        contains the annotation's content
        """
        ...
    @property
    def Date(self) -> 'Date_60040844':
        """
        contains the creation date.
        """
        ...
    @property
    def DateTimeValue(self) -> 'DateTime_84de09d3':
        """
        contains the creation date.
        """
        ...
    @property
    def Initials(self) -> str:
        """
        contains the initials of the author of the annotation.
        
        **since**
        
            LibreOffice 4.0
        """
        ...
    @property
    def Name(self) -> str:
        """
        contains the name of the annotation.
        
        **since**
        
            LibreOffice 4.0
        """
        ...


