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
# Namespace: com.sun.star.util
from .x_string_substitution import XStringSubstitution as XStringSubstitution_f660eb2

class PathSubstitution(XStringSubstitution_f660eb2):
    """
    Service Class

    A service to support the substitution and resubstitution of path variables.
    
    A path variable must be specified with the following syntax: \"$(\"<variable-name>\")\". Path variables are not case sensitive and are always provided as a UCB-compliant URLs (for example: \"file:///c:/temp\" or \"file:///usr/install\"). This is mandatory to support an optional remote file system.There is a set of variables that have pre-defined values:
    
    Attention: Most predefined variables describe an absolute path. The only exceptions are: $(username), $(langid) and $(vlang). Therefore the service implementation should only substitute variables which are located at the start of a provided path string or are part of a multi-path. This special service is not designed to be a text substitution but shall provide (a) valid substituted path(s).
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API PathSubstitution <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1PathSubstitution.html>`_
    """
    ...

