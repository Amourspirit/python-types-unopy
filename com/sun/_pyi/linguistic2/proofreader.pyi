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
# Libre Office Version: 7.2
# Namespace: com.sun.star.linguistic2
from .x_proofreader import XProofreader as XProofreader_dab0e46

class Proofreader(XProofreader_dab0e46):
    """
    Service Class

    provides a proofreader (often known as grammar checker) for text
    
    An implementation of this service will receive text and has to identify the sentence end and report all errors found.
    
    An implementation of this service is not limited to grammar checking at all. It might also check style, used terms etc. Basically it can check every aspect of a single sentence. Since the text provided is always the complete paragraph it can also choose to analyze the context of the sentence currently required to be checked. However error reports need to be limited to the current sentence.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API Proofreader <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1linguistic2_1_1Proofreader.html>`_
    """


