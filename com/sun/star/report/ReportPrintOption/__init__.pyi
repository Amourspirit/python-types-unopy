# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.report
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const

Specifies whether a page header or footer is printed on the same page as the report header or report footer.

See Also:
    `API ReportPrintOption <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1report_1_1ReportPrintOption.html>`_
"""
ALL_PAGES: Literal[0]
"""
The page header/footer is printed on all pages.
"""
NOT_WITH_REPORT_HEADER: Literal[1]
"""
The page header/footer is not printed on the same page as the report header.
"""
NOT_WITH_REPORT_FOOTER: Literal[2]
"""
The page header/footer is not printed on the same page as the report footer.
"""
NOT_WITH_REPORT_HEADER_FOOTER: Literal[3]
"""
The page header/footer is not printed on the same page as the report header or footer.
"""

