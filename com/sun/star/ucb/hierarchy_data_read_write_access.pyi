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
# Namespace: com.sun.star.ucb
from __future__ import annotations
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from ..lang.x_single_service_factory import XSingleServiceFactory as XSingleServiceFactory_27210f0d
from .hierarchy_data_read_access import HierarchyDataReadAccess as HierarchyDataReadAccess_34820f29
from ..util.x_changes_batch import XChangesBatch as XChangesBatch_bb3b0bb9

class HierarchyDataReadWriteAccess(HierarchyDataReadAccess_34820f29, XNameContainer_cb90e47, XSingleServiceFactory_27210f0d, XChangesBatch_bb3b0bb9):
    """
    Service Class

    provides read and write access to a fragment of the hierarchy data.

    See Also:
        `API HierarchyDataReadWriteAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1HierarchyDataReadWriteAccess.html>`_
    """
    ...

