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
# Namespace: com.sun.star.linguistic2
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMeaning(XInterface_8f010a43):
    """
    one of the possible meanings for a word.
    
    Represents one of the possible meanings that may be returned from a com.sun.star.linguistic2.XThesaurus.queryMeanings() call and allows for retrieval of its synonyms.

    See Also:
        `API XMeaning <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XMeaning.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XMeaning']

    def getMeaning(self) -> str:
        """
        """
        ...
    def querySynonyms(self) -> 'typing.Tuple[str, ...]':
        """
        """
        ...


