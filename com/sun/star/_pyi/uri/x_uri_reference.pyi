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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.uri
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XUriReference(XInterface_8f010a43):
    """
    represents generic, mutable URI references.
    
    See RFC 3986 for a description of URI references and related terms.
    
    This interface only handles generic URI references (both absolute and relative). For specific URI schemes, there will be additional interfaces that offer extra, scheme-specific functionality.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUriReference <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uri_1_1XUriReference.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.uri.XUriReference']

    def clearFragment(self) -> None:
        """
        clears the fragment part of this URI reference.
        """
    def getAuthority(self) -> str:
        """
        returns the authority part of this URI reference.
        """
    def getFragment(self) -> str:
        """
        returns the fragment part of this URI reference.
        """
    def getPath(self) -> str:
        """
        returns the path part of this URI reference.
        """
    def getPathSegment(self, index: int) -> str:
        """
        returns a given path segment of this URI reference.
        """
    def getPathSegmentCount(self) -> int:
        """
        returns the number of path segments of this URI reference.
        
        For a URI reference with an empty path, the number of path segments is zero. For a URI reference with an absolute, non-empty path, the number of path segments equals the number of “/” delimiters. For a URI reference with a relative, non-empty path, the number of path segments equals the number of “/” delimiters, plus one.
        """
    def getQuery(self) -> str:
        """
        returns the query part of this URI reference.
        """
    def getScheme(self) -> str:
        """
        returns the scheme part of this (absolute) URI reference.
        """
    def getSchemeSpecificPart(self) -> str:
        """
        returns the scheme-specific part of this URI reference.
        
        For an absolute URI reference, the scheme-specific part is everything after the scheme part and the delimiting “:”, and before the optional “#” and fragment part. For a relative URI reference, the scheme-specific part is everything before the optional “#” and fragment part.
        """
    def getUriReference(self) -> str:
        """
        returns the textual representation of the complete URI reference.
        """
    def hasAuthority(self) -> bool:
        """
        returns whether this URI reference has an authority part.
        """
    def hasFragment(self) -> bool:
        """
        returns whether this URI reference has a fragment part.
        """
    def hasQuery(self) -> bool:
        """
        returns whether this URI reference has a query part.
        """
    def hasRelativePath(self) -> bool:
        """
        returns whether this URI reference has a relative path.
        """
    def isAbsolute(self) -> bool:
        """
        returns whether this URI reference is absolute or relative.
        
        A URI is absolute if it has a scheme.
        """
    def isHierarchical(self) -> bool:
        """
        returns whether this URI reference is hierarchical or opaque, in the sense of RFC&nbsp2396.
        
        An absolute URI reference is hierarchical if its scheme-specific part starts with “/”. A relative URI reference is always hierarchical.
        """
    def setFragment(self, fragment: str) -> None:
        """
        sets the fragment part of this URI reference.
        """
