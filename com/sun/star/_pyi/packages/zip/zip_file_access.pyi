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
# Namespace: com.sun.star.packages.zip
from .x_zip_file_access2 import XZipFileAccess2 as XZipFileAccess2_45470f57

class ZipFileAccess(XZipFileAccess2_45470f57):
    """
    Service Class

    allows to get reading access to non-encrypted entries inside zip file.

    See Also:
        `API ZipFileAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipFileAccess.html>`_
    """
    def createWithURL(self, URL: str) -> None:
        """

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.ucb.ContentCreationException: ``ContentCreationException``
            com.sun.star.ucb.InteractiveIOException: ``InteractiveIOException``
            com.sun.star.packages.zip.ZipException: ``ZipException``
        """
        ...

