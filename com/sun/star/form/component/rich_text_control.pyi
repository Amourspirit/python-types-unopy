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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form.component
from __future__ import annotations
from ...awt.uno_control_edit_model import UnoControlEditModel as UnoControlEditModel_fd8e0dde
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ...text.text_range import TextRange as TextRange_90540a5f

class RichTextControl(UnoControlEditModel_fd8e0dde, FormControlModel_e2990d22, TextRange_90540a5f):
    """
    Service Class

    specifies a component which extends the com.sun.star.awt.UnoControlEditModel with capabilities to display and input formatted text.

    See Also:
        `API RichTextControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1RichTextControl.html>`_
    """
    @property
    def HardLineBreaks(self) -> bool:
        """
        specifies whether text should be automatically wrapped to fit into the control.
        
        If set to TRUE, users need to manually press the enter key to insert a line break. If set to FALSE, text is automatically wrapped at the control border.
        """
        ...
    @HardLineBreaks.setter
    def HardLineBreaks(self, value: bool) -> None:
        ...
    @property
    def RichText(self) -> bool:
        """
        specifies whether the control should display the text including all its formatting.
        
        If this is set to FALSE, the control will act as ordinary com.sun.star.awt.UnoControlEditModel.
        
        If the property is set to TRUE, the control will ignore the following properties:
        """
        ...
    @RichText.setter
    def RichText(self, value: bool) -> None:
        ...

