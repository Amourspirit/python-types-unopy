# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.auth
from __future__ import annotations
from .xsso_manager_factory import XSSOManagerFactory as XSSOManagerFactory_f7ef0d9a

class SSOManagerFactory(XSSOManagerFactory_f7ef0d9a):
    """
    Service Class

    represents a starting point for Single Sign-on interactions.
    
    The Single Sign-on ( SSO ) APIs provide UNO based access to underlying SSO implementations ( e.g. Kerberos ). The aim of the SSO APIs is to enable authentication ( possibly mutual ) between a client ( source or initiator ) and a network service ( target or acceptor ). This is achieved via. the creation and processing of security tokens sent between the two parties. The steps which should be followed to successfully use the SSO APIs are as follows:
    
    The interface supports the creation of XSSOManager instances which can subsequently be used to create security contexts.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SSOManagerFactory <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1auth_1_1SSOManagerFactory.html>`_
    """
    ...

