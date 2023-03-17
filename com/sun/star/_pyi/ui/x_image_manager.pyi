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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from .xui_configuration import XUIConfiguration as XUIConfiguration_c4eb0c34
from .xui_configuration_persistence import XUIConfigurationPersistence as XUIConfigurationPersistence_661010b9
if typing.TYPE_CHECKING:
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc

class XImageManager(XComponent_98dc0ab5, XInitialization_d46c0cca, XUIConfiguration_c4eb0c34, XUIConfigurationPersistence_661010b9):
    """
    specifies access functions to an images manager interface to add, replace and remove images associations to command URLs.
    
    An image manager controls a number of image sets which are specified by an ImageType.

    See Also:
        `API XImageManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XImageManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XImageManager']

    def getAllImageNames(self, nImageType: int) -> 'typing.Tuple[str, ...]':
        """
        retrieves the list of command URLs which have images associated.
        """
        ...
    def getImages(self, nImageType: int, aCommandURLSequence: 'typing.Tuple[str, ...]') -> 'typing.Tuple[XGraphic_a4da0afc, ...]':
        """
        retrieves the associated images of command URLs.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def hasImage(self, nImageType: int, CommandURL: str) -> bool:
        """
        determines if a command URL has an associated image.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def insertImages(self, nImageType: int, aCommandURLSequence: 'typing.Tuple[str, ...]', aGraphicSequence: 'typing.Tuple[XGraphic_a4da0afc, ...]') -> None:
        """
        inserts new image/command associations to an image manager.
        
        If an association is already present it is replaced. If aCommandURLSequence contains an invalid command URL a com.sun.star.lang.IllegalArgumentException is thrown. If the configuration manager is read-only a com.sun.star.lang.IllegalAccessException is thrown.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...
    def removeImages(self, nImageType: int, CommandURLs: 'typing.Tuple[str, ...]') -> None:
        """
        removes associated images to a command URL.
        
        If the aCommandURLSequence contains an invalid command URL a com.sun.star.lang.IllegalArgumentException is thrown. If the image manager is associated with a read-only configuration manager a com.sun.star.lang.IllegalAccessException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...
    def replaceImages(self, nImageType: int, aCommandURLSequence: 'typing.Tuple[str, ...]', aGraphicsSequence: 'typing.Tuple[XGraphic_a4da0afc, ...]') -> None:
        """
        replaces the associated images of command URLs.
        
        If a command URL cannot be found the replace call will be omitted. If aCommandURLSequence contains an invalid command URL a com.sun.star.lang.IllegalArgumentException is thrown. If the image manager is associated with a read-only configuration manager a com.sun.star.lang.IllegalAccessException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...
    def reset(self) -> None:
        """
        resets the image manager to default data.
        
        This means that all user images of the instance will be removed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...


