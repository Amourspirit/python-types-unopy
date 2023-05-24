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
# Namespace: com.sun.star.form.component
from __future__ import annotations
from ...awt.uno_control_file_control_model import UnoControlFileControlModel as UnoControlFileControlModel_6a4410b9
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_reset import XReset as XReset_71670917

class FileControl(UnoControlFileControlModel_6a4410b9, FormControlModel_e2990d22, XReset_71670917):
    """
    Service Class

    This service specifies the control model of an edit field for a file name.

    See Also:
        `API FileControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1FileControl.html>`_
    """
    @property
    def DefaultText(self) -> str:
        """
        contains a default value for the control.
        
        This value is used when the control is initially displayed, and for resetting it.
        """
        ...
    @DefaultText.setter
    def DefaultText(self, value: str) -> None:
        ...

