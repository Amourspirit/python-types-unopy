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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from .x_module_ui_configuration_manager2 import XModuleUIConfigurationManager2 as XModuleUIConfigurationManager2_98c61187

class ModuleUIConfigurationManager(XModuleUIConfigurationManager2_98c61187):
    """
    Service Class

    specifies a user interface configuration manager which gives access to user interface configuration data of a module.
    
    A module user interface configuration manager supports two layers of configuration settings data:
    
    **since**
    
        OOo 2.0

    See Also:
        `API ModuleUIConfigurationManager <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1ModuleUIConfigurationManager.html>`_
    """
    def createDefault(self, ModuleShortName: str, ModuleIdentifier: str) -> None:
        """
        provides a function to initialize a module user interface configuration manager instance.
        
        A module user interface configuration manager instance needs the following arguments as com.sun.star.beans.PropertyValue to be in a working state:
        
        A non-initialized module user interface configuration manager cannot be used, it is treated as a read-only container.

        Raises:
            com.sun.star.configuration.CorruptedUIConfigurationException: ``CorruptedUIConfigurationException``
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

