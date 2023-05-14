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
# Singleton Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.4
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6


class theWindowStateConfiguration(XNameAccess_e2ab0cf6):
    """
    Singleton Class

    a singleton which provides window based information about user interface elements.
    
    OpenOffice.org has an amount of user interface elements that can be positioned, resized, closed and their style can be changed. This singleton provides access to the window based information of available user interface elements which are part of OpenOffice.org modules, like Writer or Calc.
    
    Provides access to window based information about user interface elements of all installed application modules.
    
    To access the window based information of a module, a unique module specifier must be provided to com.sun.star.container.XNameAccess.getByName() function. The module specifier can be retrieved from the com.sun.star.frame.ModuleManager service. The interface provides references to a com.sun:star.ui.ModuleWindowStateConfiguration.
    
    Prior to LibreOffice 4.3, this singleton was only available as a (single-instance) WindowStateConfiguration service.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API theWindowStateConfiguration <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1ui_1_1theWindowStateConfiguration.html>`_
    """
    ...


