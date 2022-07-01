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
# Namespace: com.sun.star.deployment
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
if typing.TYPE_CHECKING:
    from ..beans.string_pair import StringPair as StringPair_a4bc0b14
    from .x_package_type_info import XPackageTypeInfo as XPackageTypeInfo_3bc70f7b
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..task.x_abort_channel import XAbortChannel as XAbortChannel_baca0bc4
    from ..ucb.x_command_environment import XCommandEnvironment as XCommandEnvironment_fb330dee

class XPackage(XComponent_98dc0ab5, XModifyBroadcaster_fd990df0):
    """
    Objects of this interface reflect a bound package and are issued by a PackageRegistryBackend.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XPackage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XPackage.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.deployment.XPackage']

    def checkDependencies(self, xCmdEnv: 'XCommandEnvironment_fb330dee') -> bool:
        """
        checks if the dependencies for this package are still satisfied
        
        After updating the OpenOffice.org, some dependencies for packages might no longer be satisfied.
        
        **since**
        
            OOo 3.2

        Raises:
            DeploymentException: ``DeploymentException``
            ExtensionRemovedException: ``ExtensionRemovedException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
        """
    def checkPrerequisites(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee', alreadyInstalled: bool) -> int:
        """
        checks if the package can be installed.
        
        Only if the return value is TRUE the package is allowed to be installed. In case of FALSE or in case of an exception, the package must be removed completely. After return of this function no code from the extension may be used anymore, so that the extension can be safely removed from the hard disk.

        Raises:
            DeploymentException: ``DeploymentException``
            ExtensionRemovedException: ``ExtensionRemovedException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
        """
    def createAbortChannel(self) -> 'XAbortChannel_baca0bc4':
        """
        creates a command channel to be used to asynchronously abort a command.
        """
    def exportTo(self, destFolderURL: str, newTitle: str, nameClashAction: int, xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        exports package to given destination URL.

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.ucb.ContentCreationException: ``ContentCreationException``
        """
    def getBundle(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'typing.Tuple[XPackage, ...]':
        """
        Gets packages of the bundle.
        
        If isRemoved() returns TRUE then getBundle may return an empty sequence in case the object is not registered.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def getDescription(self) -> str:
        """
        returns a description string to describe the package.

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getDisplayName(self) -> str:
        """
        returns the display name of the package, e.g.
        
        for graphical user interfaces (GUI).

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getIcon(self, highContrast: bool) -> 'XGraphic_a4da0afc':
        """
        returns an icon for a package.

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getIdentifier(self) -> object:
        """
        returns the unique extension identifier.
        """
    def getLicenseText(self) -> str:
        """
        returns a string containing the license text.

        Raises:
            DeploymentException: ``DeploymentException``
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getName(self) -> str:
        """
        returns the file name of the package.
        """
    def getPackageType(self) -> 'XPackageTypeInfo_3bc70f7b':
        """
        returns the XPackageTypeInfo, e.g.
        
        media-type etc.
        """
    def getPublisherInfo(self) -> 'StringPair_a4bc0b14':
        """
        returns the publisher info for the package, the strings might be empty, if there is no publisher
        
        com.sun.star.beans.StringPair.First represents the publisher name and com.sun.star.beans.StringPair.Second represents the URL to the publisher.

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getRegistrationDataURL(self) -> object:
        """
        return a URL to a directory which contains the registration data.
        
        This data may be created when calling XPackage.registerPackage(). If this is the case is indicated by com.sun.star.beans.Optional.IsPresent of the return value. If registration data are created during registration, but the package is currently not registered, for example after calling XPackage.revokePackage(), then com.sun.star.beans.Optional.IsPresent is TRUE and the com.sun.star.beans.Optional.Value may be an empty string.

        Raises:
            DeploymentException: ``DeploymentException``
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getRepositoryName(self) -> str:
        """
        returns the name of the repository where this object comes from.
        """
    def getURL(self) -> str:
        """
        returns the location of the package.
        """
    def getUpdateInformationURLs(self) -> 'typing.Tuple[str, ...]':
        """
        returns a sequence of update information URLs.
        
        The sequence may be empty in case no update information is available. If the sequence contains more than one URL, the extra URLs must mirror the information available at the first URL.

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def getVersion(self) -> str:
        """
        returns the textual version representation of the package.
        
        A textual version representation is a finite string following the BNFversion .= [element (\".\" element)*]element .= (\"0\" | \"1\" | \"2\" | \"3\" | \"4\" | \"5\" | \"6\" | \"7\" | \"8\" | \"9\")+

        Raises:
            ExtensionRemovedException: ``ExtensionRemovedException``
        """
    def isBundle(self) -> bool:
        """
        reflects whether this package is a bundle of one or more packages, e.g.
        
        a zip (legacy) package file or a document hosting script packages.
        """
    def isRegistered(self, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> object:
        """
        determines whether the package is currently registered, i.e.
        
        whether it is active.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
        """
    def isRemoved(self) -> bool:
        """
        indicates if this object represents a removed extension or extension item.
        
        This is the case when it was created by providing TRUE for the removed parameter in the function XPackageRegistry.bindPackage().
        """
    def registerPackage(self, startup: bool, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        registers this XPackage.
        
        NEVER call this directly. This is done by the extension manager if necessary.

        Raises:
            DeploymentException: ``DeploymentException``
            ExtensionRemovedException: ``ExtensionRemovedException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def revokePackage(self, startup: bool, xAbortChannel: 'XAbortChannel_baca0bc4', xCmdEnv: 'XCommandEnvironment_fb330dee') -> None:
        """
        revokes this XPackage.
        
        NEVER call this directly. This is done by the extension manager if necessary.

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.ucb.CommandAbortedException: ``CommandAbortedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

