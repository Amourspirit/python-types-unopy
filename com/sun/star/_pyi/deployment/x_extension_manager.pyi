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
# Namespace: com.sun.star.deployment
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from .x_package import XPackage as XPackage_cb1f0c4d
    from .x_package_type_info import XPackageTypeInfo as XPackageTypeInfo_3bc70f7b
    from ..task.x_abort_channel import XAbortChannel as XAbortChannel_baca0bc4
    from ..ucb.x_command_environment import XCommandEnvironment as XCommandEnvironment_fb330dee

class XExtensionManager(XComponent_98dc0ab5, XModifyBroadcaster_fd990df0):
    """
    The XExtensionManager interface is used to manage extensions in the user, shared and bundled repository.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XExtensionManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XExtensionManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.deployment.XExtensionManager']

    def addExtension(self, url: str, properties: 'typing.Tuple[NamedValue_a37a0af3, ...]', repository: str, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'XPackage_cb1f0c4d':
        """
        adds an extension.
        
        The properties argument is currently only used to suppress the license information for shared extensions.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def checkPrerequisitesAndEnable(self, extension: 'XPackage_cb1f0c4d', xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> int:
        """
        check if all prerequisites for the extension are fulfilled and activates it, if possible.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createAbortChannel(self) -> 'XAbortChannel_baca0bc4':
        """
        creates a command channel to be used to asynchronously abort a command.
        """
        ...
    def disableExtension(self, extension: 'XPackage_cb1f0c4d', xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        disable an extension.
        
        If the extension is not from the user repository then an IllegalArgumentException is thrown.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def enableExtension(self, extension: 'XPackage_cb1f0c4d', xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        enable an extension.
        
        If the extension is not from the user repository then an IllegalArgumentException is thrown.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getAllExtensions(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[typing.Tuple[XPackage_cb1f0c4d, ...], ...]':
        """
        returns a sequence containing all installed extensions.
        
        The members of the returned sequence correspond to an extension with a particular extension identifier. The members are also sequences which contain as many elements as there are repositories. Those are ordered according to the priority of the repository. That is, the first member is the extension from the user repository, the second is from the shared repository and the last is from the bundled repository.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getDeployedExtension(self, repository: str, identifier: str, fileName: str, xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'XPackage_cb1f0c4d':
        """
        gets an installed extensions.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getDeployedExtensions(self, repository: str, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[XPackage_cb1f0c4d, ...]':
        """
        gets all currently installed extensions, including disabled user extensions.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getExtensionsWithSameIdentifier(self, identifier: str, fileName: str, xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[XPackage_cb1f0c4d, ...]':
        """
        gets all extensions with the same identifier from all repositories.
        
        The extension at the first position in the returned sequence represents the extension from the user repository. The next element is from the shared and the last one is from the bundled repository. If one repository does not contain this extension, then the respective element is a null reference.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getExtensionsWithUnacceptedLicenses(self, repository: str, xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[XPackage_cb1f0c4d, ...]':
        """
        returns all extensions which are currently not in use because the user did not accept the license.
        
        The function will not return any object for the user repository, because a user extension will not be kept in the user repository if its license is declined. Only extensions which are registered at start-up of OOo, that is, shared and bundled extensions, can be returned.
        
        Extensions which allow the license to be suppressed, that is, it does not need to be displayed, and which are installed with the corresponding option, are also not returned.
        
        Extensions returned by these functions are not returned by XExtensionManager.getDeployedExtension() XExtensionManager.getDeployedExtensions() XExtensionManager.getAllExtensions() XExtensionManager.getExtensionsWithSameIdentifier()

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getSupportedPackageTypes(self) -> 'typing.Tuple[XPackageTypeInfo_3bc70f7b, ...]':
        """
        gets the supported XPackageTypeInfos.
        """
        ...
    def isReadOnlyRepository(self, repository: str) -> bool:
        """
        determines if the current user has write access to the extensions folder of the repository.
        """
        ...
    def reinstallDeployedExtensions(self, force: bool, repository: str, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        Expert feature: erases the underlying registry cache and reinstalls all previously added extensions.
        
        Please keep in mind that all registration status get lost.
        
        Please use this in case of suspected cache inconsistencies only.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def removeExtension(self, identifier: str, fileName: str, repository: str, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        removes an extension.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def synchronize(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> bool:
        """
        synchronizes the extension database with the contents of the extensions folder of shared and bundled extensions.
        
        Added extensions will be added to the database and removed extensions will be removed from the database. The active extensions are determined. That is, shared or bundled extensions are not necessarily registered (XPackage.registerPackage()).

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


