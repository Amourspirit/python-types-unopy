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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.xml.crypto
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class SecurityOperationStatus(Enum):
    """
    Enum

    

    See Also:
        `API SecurityOperationStatus <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1crypto.html#ab5d887eb5da1173b766d96d0d863d1dc>`_
    """
    typeName: str = 'com.sun.star.xml.crypto.SecurityOperationStatus'

    ASSERTION: 'uno.Enum'
    """
    """
    CERT_HAS_EXPIRED: 'uno.Enum'
    """
    """
    CERT_ISSUER_FAILED: 'uno.Enum'
    """
    """
    CERT_NOT_FOUND: 'uno.Enum'
    """
    """
    CERT_NOT_YET_VALID: 'uno.Enum'
    """
    """
    CERT_REVOKED: 'uno.Enum'
    """
    """
    CERT_VERIFY_FAILED: 'uno.Enum'
    """
    """
    CRYPTO_FAILED: 'uno.Enum'
    """
    """
    DATA_NOT_MATCH: 'uno.Enum'
    """
    """
    DISABLED: 'uno.Enum'
    """
    """
    DSIG_INVALID_REFERENCE: 'uno.Enum'
    """
    """
    DSIG_NO_REFERENCES: 'uno.Enum'
    """
    """
    ENGINE_FAILED: 'uno.Enum'
    """
    The following constants are derived from XMLSec error definitions, as following:
    
    XMLSEC_ERRORS_R_XMLSEC_FAILED XMLSEC_ERRORS_R_MALLOC_FAILED XMLSEC_ERRORS_R_STRDUP_FAILED XMLSEC_ERRORS_R_CRYPTO_FAILED XMLSEC_ERRORS_R_XML_FAILED XMLSEC_ERRORS_R_XSLT_FAILED XMLSEC_ERRORS_R_IO_FAILED XMLSEC_ERRORS_R_DISABLED XMLSEC_ERRORS_R_NOT_IMPLEMENTED XMLSEC_ERRORS_R_INVALID_SIZE XMLSEC_ERRORS_R_INVALID_DATA XMLSEC_ERRORS_R_INVALID_RESULT XMLSEC_ERRORS_R_INVALID_TYPE XMLSEC_ERRORS_R_INVALID_OPERATION XMLSEC_ERRORS_R_INVALID_STATUS XMLSEC_ERRORS_R_INVALID_FORMAT XMLSEC_ERRORS_R_DATA_NOT_MATCH XMLSEC_ERRORS_R_INVALID_NODE XMLSEC_ERRORS_R_INVALID_NODE_CONTENT XMLSEC_ERRORS_R_INVALID_NODE_ATTRIBUTE XMLSEC_ERRORS_R_MISSING_NODE_ATTRIBUTE XMLSEC_ERRORS_R_NODE_ALREADY_PRESENT XMLSEC_ERRORS_R_UNEXPECTED_NODE XMLSEC_ERRORS_R_NODE_NOT_FOUND XMLSEC_ERRORS_R_INVALID_TRANSFORM XMLSEC_ERRORS_R_INVALID_TRANSFORM_KEY XMLSEC_ERRORS_R_INVALID_URI_TYPE XMLSEC_ERRORS_R_TRANSFORM_SAME_DOCUMENT_REQUIRED XMLSEC_ERRORS_R_TRANSFORM_DISABLED XMLSEC_ERRORS_R_INVALID_KEY_DATA XMLSEC_ERRORS_R_KEY_DATA_NOT_FOUND XMLSEC_ERRORS_R_KEY_DATA_ALREADY_EXIST XMLSEC_ERRORS_R_INVALID_KEY_DATA_SIZE XMLSEC_ERRORS_R_KEY_NOT_FOUND XMLSEC_ERRORS_R_KEYDATA_DISABLED XMLSEC_ERRORS_R_MAX_RETRIEVALS_LEVEL XMLSEC_ERRORS_R_MAX_RETRIEVAL_TYPE_MISMATCH XMLSEC_ERRORS_R_MAX_ENCKEY_LEVEL XMLSEC_ERRORS_R_CERT_VERIFY_FAILED XMLSEC_ERRORS_R_CERT_NOT_FOUND XMLSEC_ERRORS_R_CERT_REVOKED XMLSEC_ERRORS_R_CERT_ISSUER_FAILED XMLSEC_ERRORS_R_CERT_NOT_YET_VALID XMLSEC_ERRORS_R_CERT_HAS_EXPIRED XMLSEC_ERRORS_R_DSIG_NO_REFERENCES XMLSEC_ERRORS_R_DSIG_INVALID_REFERENCE XMLSEC_ERRORS_R_ASSERTION XMLSEC_ERRORS_MAX_NUMBER
    """
    INVALID_DATA: 'uno.Enum'
    """
    """
    INVALID_FORMAT: 'uno.Enum'
    """
    """
    INVALID_KEY_DATA: 'uno.Enum'
    """
    """
    INVALID_KEY_DATA_SIZE: 'uno.Enum'
    """
    """
    INVALID_NODE: 'uno.Enum'
    """
    """
    INVALID_NODE_ATTRIBUTE: 'uno.Enum'
    """
    """
    INVALID_NODE_CONTENT: 'uno.Enum'
    """
    """
    INVALID_OPERATION: 'uno.Enum'
    """
    """
    INVALID_RESULT: 'uno.Enum'
    """
    """
    INVALID_SIZE: 'uno.Enum'
    """
    """
    INVALID_STATUS: 'uno.Enum'
    """
    """
    INVALID_TRANSFORM: 'uno.Enum'
    """
    """
    INVALID_TRANSFORM_KEY: 'uno.Enum'
    """
    """
    INVALID_TYPE: 'uno.Enum'
    """
    """
    INVALID_URI_TYPE: 'uno.Enum'
    """
    """
    IO_FAILED: 'uno.Enum'
    """
    """
    KEYDATA_DISABLED: 'uno.Enum'
    """
    """
    KEY_DATA_ALREADY_EXIST: 'uno.Enum'
    """
    """
    KEY_DATA_NOT_FOUND: 'uno.Enum'
    """
    """
    KEY_NOT_FOUND: 'uno.Enum'
    """
    """
    MALLOC_FAILED: 'uno.Enum'
    """
    """
    MAX_ENCKEY_LEVEL: 'uno.Enum'
    """
    """
    MAX_RETRIEVALS_LEVEL: 'uno.Enum'
    """
    """
    MAX_RETRIEVAL_TYPE_MISMATCH: 'uno.Enum'
    """
    """
    MISSING_NODE_ATTRIBUTE: 'uno.Enum'
    """
    """
    NODE_ALREADY_PRESENT: 'uno.Enum'
    """
    """
    NODE_NOT_FOUND: 'uno.Enum'
    """
    """
    NOT_IMPLEMENTED: 'uno.Enum'
    """
    """
    OPERATION_SUCCEEDED: 'uno.Enum'
    """
    """
    RUNTIMEERROR_FAILED: 'uno.Enum'
    """
    """
    STRDUP_FAILED: 'uno.Enum'
    """
    """
    TRANSFORM_DISABLED: 'uno.Enum'
    """
    """
    TRANSFORM_SAME_DOCUMENT_REQUIRED: 'uno.Enum'
    """
    """
    UNEXPECTED_NODE: 'uno.Enum'
    """
    """
    UNKNOWN: 'uno.Enum'
    """
    """
    XML_FAILED: 'uno.Enum'
    """
    """
    XSLT_FAILED: 'uno.Enum'
    """
    """

