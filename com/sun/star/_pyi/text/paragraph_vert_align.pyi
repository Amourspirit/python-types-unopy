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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class ParagraphVertAlign(object):
    """
    Const

    These enumeration values are used to specify the vertical alignment of paragraphs.

    See Also:
        `API ParagraphVertAlign <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1ParagraphVertAlign.html>`_
    """
    AUTOMATIC: Literal[0]
    """
    In automatic mode, horizontal text is aligned to the baseline.
    
    The same applies to text that is rotated 90°. Text that is rotated 270 ° is aligned to the center.
    """
    BASELINE: Literal[1]
    """
    The text is aligned to the baseline.
    """
    TOP: Literal[2]
    """
    The text is aligned to the top.
    """
    CENTER: Literal[3]
    """
    The text is aligned to the center.
    """
    BOTTOM: Literal[4]
    """
    The text is aligned to bottom.
    """

