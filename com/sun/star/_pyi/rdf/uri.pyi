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
# Namespace: com.sun.star.rdf
from .xuri import XURI as XURI_5682078c

class URI(XURI_5682078c):
    """
    Service Class

    represents a URI node that may occur in a RDF graph.
    
    **since**
    
        OOo 3.0

    See Also:
        `API URI <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1rdf_1_1URI.html>`_
    """
    def create(self, Value: str) -> None:
        """
        creates a URI RDF node.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createKnown(self, Id: int) -> None:
        """
        creates a URI RDF node for a well-known URI.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createNS(self, Namespace: str, LocalName: str) -> None:
        """
        creates a URI RDF node from namespace prefix and local name.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

