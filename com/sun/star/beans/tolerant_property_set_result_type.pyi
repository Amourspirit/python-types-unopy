# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.beans
import typing


class TolerantPropertySetResultType:
    """
    Const

    specifies the possible failure types when using the com.sun.star.beans.XTolerantMultiPropertySet interface.
    
    It usually matches one of the exception types that may occur when using the com.sun.star.beans.XPropertySet or com.sun.star.beans.XMultiPropertySet interfaces.

    See Also:
        `API TolerantPropertySetResultType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans_1_1TolerantPropertySetResultType.html>`_
    """
    SUCCESS: int = ...
    """
    the property has been successfully set or retrieved.
    """
    UNKNOWN_PROPERTY: int = ...
    """
    the property is not available.
    
    For example if a com.sun.star.beans.UnknownPropertyException was caught.
    """
    ILLEGAL_ARGUMENT: int = ...
    """
    the value used with the property is not valid.
    
    For example if a com.sun.star.lang.IllegalArgumentException was caught.
    """
    PROPERTY_VETO: int = ...
    """
    the property could not be changed at that time.
    
    For example if a com.sun.star.beans.PropertyVetoException was caught.
    """
    WRAPPED_TARGET: int = ...
    """
    a com.sun.star.lang.WrappedTargetException did occur.
    """
    UNKNOWN_FAILURE: int = ...
    """
    the operation failed and the reason is not known.
    """

