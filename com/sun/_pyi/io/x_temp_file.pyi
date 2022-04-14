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
# Libre Office Version: 7.2
# Namespace: com.sun.star.io
from typing_extensions import Literal
from .x_seekable import XSeekable as XSeekable_79540954
from .x_stream import XStream as XStream_678908a4

class XTempFile(XSeekable_79540954, XStream_678908a4):
    """
    This interface offers access to temp files.

    See Also:
        `API XTempFile <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XTempFile.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.io.XTempFile']

    @property
    def RemoveFile(self) -> bool:
        """
        This attribute controls whether the file will be automatically removed on object destruction.
        """

    @property
    def ResourceName(self) -> str:
        """
        This attribute specifies the temp file name.
        """

    @property
    def Uri(self) -> str:
        """
        This attribute specifies the URL of the temp file.
        """


__all__ = ['XTempFile']

