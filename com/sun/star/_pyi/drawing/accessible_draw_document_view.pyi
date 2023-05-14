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
# Namespace: com.sun.star.drawing
from ..accessibility.x_accessible import XAccessible as XAccessible_1cbc0eb6
from ..accessibility.x_accessible_component import XAccessibleComponent as XAccessibleComponent_b2f21269
from ..accessibility.x_accessible_context import XAccessibleContext as XAccessibleContext_8eae119b

class AccessibleDrawDocumentView(XAccessible_1cbc0eb6, XAccessibleComponent_b2f21269, XAccessibleContext_8eae119b):
    """
    Service Class

    The AccessibleDrawDocumentView service is implemented by views of Draw and Impress documents.
    
    An object that implements the AccessibleDrawDocumentView service provides information about the view of a Draw or Impress document in one of the various view modes. With its children it gives access to the current page and the shapes on that page.
    
    This service gives a simplified view on the underlying document. It tries both to keep the structure of the accessibility representation tree as simple as possible and provide as much relevant information as possible. This has the following consequences:
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleDrawDocumentView <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1AccessibleDrawDocumentView.html>`_
    """
    ...

