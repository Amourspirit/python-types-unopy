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
# Namespace: com.sun.star.form.binding
from .bindable_data_aware_control_model import BindableDataAwareControlModel as BindableDataAwareControlModel_47091512
from ..component.database_radio_button import DatabaseRadioButton as DatabaseRadioButton_b03c123d

class BindableDatabaseRadioButton(BindableDataAwareControlModel_47091512, DatabaseRadioButton_b03c123d):
    """
    Service Class

    This service specifies a radio button which is data-aware and thus can be bound to a database field, and additionally supports binding to arbitrary external values.
    
    The com.sun.star.form.binding.XValueBinding instance which can be associated with a BindableDatabaseRadioButton must support exchanging boolean values. The following mapping between external values and control states apply:
    
    If the value binding associated with a BindableDatabaseRadioButton supports exchanging string values, and the com.sun.star.form.component.RadioButton.RefValue is not empty, then the radio button will exchange its value as string:

    See Also:
        `API BindableDatabaseRadioButton <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1binding_1_1BindableDatabaseRadioButton.html>`_
    """
    @property
    def SecondaryRefValue(self) -> str:
        """
        specifies a value which is to be associated with the control when it's not selected.
        
        com.sun.star.form.component.RadioButton.RefValue is transferred to possible external value bindings as soon as the radio button is selected. With the member SecondaryRefValue, clients of the radio button can also associate a value with the not selected state of the control.
        """
        ...
    @SecondaryRefValue.setter
    def SecondaryRefValue(self, value: str) -> None:
        ...

