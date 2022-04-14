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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.security
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class AllPermission(object):
    """
    Struct Class

    The AllPermission is a permission that implies all other permissions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AllPermission <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1security_1_1AllPermission.html>`_
    """
    typeName: Literal['com.sun.star.security.AllPermission']

    def __init__(self, dummy: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            dummy (int, optional): dummy value.
        """


    @property
    def dummy(self) -> int:
        ...



__all__ = ['AllPermission']
