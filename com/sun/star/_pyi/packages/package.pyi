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
# Libre Office Version: 7.2
# Namespace: com.sun.star.packages
from ..container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess_9e2611b5
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ..lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory_27210f0d
from ..util.x_changes_batch import XChangesBatch as XChangesBatch_bb3b0bb9

class Package(XHierarchicalNameAccess_9e2611b5, XInitialization_d46c0cca, XSingleServiceFactory_27210f0d, XChangesBatch_bb3b0bb9):
    """
    Service Class

    The Package is a service that provides access to a set of files and folders contained within a Package.
    
    One instance of the Package service exists for each Package file to be manipulated.
    
    Each instance is created with an argument which specifies the URL of the Package file to which the user requires access. If the instance is created without arguments, it must be initialized with the com.sun.star.lang.XInitialization service methods before it is a valid instance of the service.

    See Also:
        `API Package <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1packages_1_1Package.html>`_
    """
    ...


