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
# Namespace: com.sun.star.form.validation
from __future__ import annotations
from ..binding.bindable_control_model import BindableControlModel as BindableControlModel_9a1111a8
from .validatable_control_model import ValidatableControlModel as ValidatableControlModel_12621440

class ValidatableBindableControlModel(BindableControlModel_9a1111a8, ValidatableControlModel_12621440):
    """
    Service Class

    specifies a control model which supports both binding to an external value supplier, and to an external validator.
    
    There are two methods how the value which is represented by a control model can interact with other components (well, except the trivial ones accessible by using com.sun.star.beans.XPropertySet):
    
    The ValidatableBindableControlModel services describes the interaction of these concepts for control models which support both of them.

    See Also:
        `API ValidatableBindableControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1validation_1_1ValidatableBindableControlModel.html>`_
    """
    ...

