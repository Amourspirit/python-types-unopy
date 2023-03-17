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
# Namespace: com.sun.star.text
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_auto_text_group import XAutoTextGroup as XAutoTextGroup_c9770c70

class AutoTextGroup(XIndexAccess_f0910d6d, XNamed_a6520b08, XAutoTextGroup_c9770c70):
    """
    Service Class

    provides access to text blocks in a group.

    See Also:
        `API AutoTextGroup <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1AutoTextGroup.html>`_
    """
    @property
    def FilePath(self) -> str:
        """
        The path to the file containing the AutoTextEntry's in this group.
        """
        ...
    @property
    def Title(self) -> str:
        """
        The title of this AutoTextGroup.
        """
        ...

