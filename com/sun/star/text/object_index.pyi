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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
from .base_index import BaseIndex as BaseIndex_8f0d0a40

class ObjectIndex(BaseIndex_8f0d0a40):
    """
    Service Class

    specifies service of object indexes within a document.

    See Also:
        `API ObjectIndex <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1ObjectIndex.html>`_
    """
    @property
    def CreateFromOtherEmbeddedObjects(self) -> bool:
        """
        Determines if external embedded objects are included in the office.
        """
        ...
    @CreateFromOtherEmbeddedObjects.setter
    def CreateFromOtherEmbeddedObjects(self, value: bool) -> None:
        ...
    @property
    def CreateFromStarCalc(self) -> bool:
        """
        Determines if star office calc objects are included in the office.
        """
        ...
    @CreateFromStarCalc.setter
    def CreateFromStarCalc(self, value: bool) -> None:
        ...
    @property
    def CreateFromStarChart(self) -> bool:
        """
        Determines if star office chart objects are included in the office.
        """
        ...
    @CreateFromStarChart.setter
    def CreateFromStarChart(self, value: bool) -> None:
        ...
    @property
    def CreateFromStarDraw(self) -> bool:
        """
        Determines if star office draw objects are included in the office.
        """
        ...
    @CreateFromStarDraw.setter
    def CreateFromStarDraw(self, value: bool) -> None:
        ...
    @property
    def CreateFromStarImage(self) -> bool:
        """
        Determines if star office image objects are included in the office.
        """
        ...
    @CreateFromStarImage.setter
    def CreateFromStarImage(self, value: bool) -> None:
        ...
    @property
    def CreateFromStarMath(self) -> bool:
        """
        Determines if star office math objects are included in the office.
        """
        ...
    @CreateFromStarMath.setter
    def CreateFromStarMath(self, value: bool) -> None:
        ...
