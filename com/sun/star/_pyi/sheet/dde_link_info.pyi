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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .dde_item_info import DDEItemInfo as DDEItemInfo_ac870b09


class DDELinkInfo(object):
    """
    Struct Class

    describes all items of a DDE connection used in formulas.
    
    A DDE connection consists of the DDE service name, the DDE topic and a list of DDE items which may contain results cached from the last update.
    
    The formula that would need this information for example would contain =[1]!'R1C1' or =[2]!'Sheet1.A1' where [1] is an external link with DDE service name \"excel\" and the topic \"X:\\PATH\\[FILE.XLSX]Sheet1\", and [2] contains service \"soffice\" and topic \"file:///X:/PATH/FILE.ODS\". The service name is stored in DDELinkInfo.Service, the topic is stored in DDELinkInfo.Topic. Note that if the DDE item contains single quotes they are escaped by doubling them, as usual, for example =[2]!'''Sheet name''.A1' in a \"soffice\" service.
    
    **since**
    
        OOo 3.1

    See Also:
        `API DDELinkInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DDELinkInfo.html>`_
    """
    typeName: Literal['com.sun.star.sheet.DDELinkInfo']

    def __init__(self, Items: typing.Optional[typing.Tuple[DDEItemInfo_ac870b09, ...]] = ..., Service: typing.Optional[str] = ..., Topic: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Items (typing.Tuple[DDEItemInfo, ...], optional): Items value.
            Service (str, optional): Service value.
            Topic (str, optional): Topic value.
        """


    @property
    def Items(self) -> typing.Tuple[DDEItemInfo_ac870b09, ...]:
        """
        A list of DDE items.
        
        Each item may contain its results from the last update.
        """


    @property
    def Service(self) -> str:
        """
        The DDE service name.
        """


    @property
    def Topic(self) -> str:
        """
        The DDE topic.
        """

