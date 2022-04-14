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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .search_criterium import SearchCriterium as SearchCriterium_c6d30c4c
from .search_recursion import SearchRecursion as SearchRecursion_c7080c52


class SearchInfo(object):
    """
    Struct Class

    information needed to (recursively) search an object.

    See Also:
        `API SearchInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1SearchInfo.html>`_
    """
    typeName: Literal['com.sun.star.ucb.SearchInfo']

    def __init__(self, Criteria: typing.Optional[typing.Tuple[SearchCriterium_c6d30c4c, ...]] = ..., Recursion: typing.Optional[SearchRecursion_c7080c52] = ..., IncludeBase: typing.Optional[bool] = ..., RespectFolderViewRestrictions: typing.Optional[bool] = ..., RespectDocViewRestrictions: typing.Optional[bool] = ..., FollowIndirections: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Criteria (typing.Tuple[SearchCriterium, ...], optional): Criteria value.
            Recursion (SearchRecursion, optional): Recursion value.
            IncludeBase (bool, optional): IncludeBase value.
            RespectFolderViewRestrictions (bool, optional): RespectFolderViewRestrictions value.
            RespectDocViewRestrictions (bool, optional): RespectDocViewRestrictions value.
            FollowIndirections (bool, optional): FollowIndirections value.
        """


    @property
    def Criteria(self) -> typing.Tuple[SearchCriterium_c6d30c4c, ...]:
        """
        the search criteria.
        """


    @property
    def Recursion(self) -> SearchRecursion_c7080c52:
        """
        the mode of recursion to use.
        """


    @property
    def IncludeBase(self) -> bool:
        """
        whether to include the object itself in the search or only (some of) its sub-objects.
        """


    @property
    def RespectFolderViewRestrictions(self) -> bool:
        """
        whether to respect the \"view restrictions\" specified for the folders hierarchically contained within an object (e.g., only searches through subscribed folders).
        """


    @property
    def RespectDocViewRestrictions(self) -> bool:
        """
        whether to respect the \"view restrictions\" specified for the documents hierarchically contained within an object (e.g., only searches through marked documents).
        """


    @property
    def FollowIndirections(self) -> bool:
        """
        whether to follow indirections (link objects) and search through their respective targets also.
        """



__all__ = ['SearchInfo']
