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
# Libre Office Version: 7.3
# Namespace: com.sun.star.util
from .x_office_installation_directories import XOfficeInstallationDirectories as XOfficeInstallationDirectories_c38f12d9

class OfficeInstallationDirectories(XOfficeInstallationDirectories_c38f12d9):
    """
    Service Class

    encapsulates access to the current office installation directory and office user data directory, provides functionality to create URLs containing relocatable (not absolute) references to the current office installation directory and user data directory and vice versa.
    
    This functionality is useful when data containing references to the current office installation directory or user data directory must be made persistent and re-read later. In many cases, storing the reference directly would destroy the relocatability of an office installation and the possibility to share one office user data directory among parallel office installations.
    
    **since**
    
        OOo 2.0
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API OfficeInstallationDirectories <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1OfficeInstallationDirectories.html>`_
    """
    ...


