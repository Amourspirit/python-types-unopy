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
# Libre Office Version: 7.2
# Namespace: com.sun.star.smarttags
from typing_extensions import Literal
import typing
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
if typing.TYPE_CHECKING:
    from ..frame.x_controller import XController as XController_b00e0b8f
    from .smart_tag_recognizer_mode import SmartTagRecognizerMode as SmartTagRecognizerMode_9179119e
    from ..text.x_text_markup import XTextMarkup as XTextMarkup_a5d60b3a
    from ..text.x_text_range import XTextRange as XTextRange_9a910ab7

class XRangeBasedSmartTagRecognizer(XInitialization_d46c0cca):
    """
    provides access to a range based smart tag recognizer.

    See Also:
        `API XRangeBasedSmartTagRecognizer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1smarttags_1_1XRangeBasedSmartTagRecognizer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.smarttags.XRangeBasedSmartTagRecognizer']

    def recognizeTextRange(self, xRange: 'XTextRange_9a910ab7', eDataType: 'SmartTagRecognizerMode_9179119e', xTextMarkup: 'XTextMarkup_a5d60b3a', aApplicationName: str, xController: 'XController_b00e0b8f') -> None:
        """
        recognizes smart tags.
        """

__all__ = ['XRangeBasedSmartTagRecognizer']

