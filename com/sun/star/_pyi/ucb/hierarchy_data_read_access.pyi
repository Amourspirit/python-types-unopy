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
# Namespace: com.sun.star.ucb
from ..container.x_hierarchical_name_access import XHierarchicalNameAccess as XHierarchicalNameAccess_9e2611b5
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..util.x_changes_notifier import XChangesNotifier as XChangesNotifier_e1b50d17

class HierarchyDataReadAccess(XHierarchicalNameAccess_9e2611b5, XNameAccess_e2ab0cf6, XComponent_98dc0ab5, XChangesNotifier_e1b50d17):
    """
    Service Class

    provides read access to a fragment of the hierarchy data.
    
    A hierarchy data source provides access to a tree of hierarchy data nodes. Each hierarchy data node, except the root node, has a parent that is a hierarchy data node too. A hierarchy data node has a name.
    
    Each hierarchy data node has three data members:

    See Also:
        `API HierarchyDataReadAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1HierarchyDataReadAccess.html>`_
    """
    ...


