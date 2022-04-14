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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from typing_extensions import Literal


class WrapInfluenceOnPosition:
    """
    Const Class

    These values specify the influence of the wrapping style of a floating screen object when it's positioned.

    See Also:
        `API WrapInfluenceOnPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1WrapInfluenceOnPosition.html>`_
    """
    ONCE_SUCCESSIVE: Literal[1]
    """
    wrapping style has no influence on the position and the floating screen object is successive positioned.
    """
    ONCE_CONCURRENT: Literal[2]
    """
    wrapping style has no influence on the position and the floating screen object is concurrent positioned.
    """
    ITERATIVE: Literal[3]
    """
    wrapping style has influence on the position and the floating screen object is iterative positioned.
    """

__all__ = ['WrapInfluenceOnPosition']
