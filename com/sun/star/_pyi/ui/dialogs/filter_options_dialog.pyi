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
# Namespace: com.sun.star.ui.dialogs
from ...beans.x_property_access import XPropertyAccess as XPropertyAccess_e1d40d20
from .x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1

class FilterOptionsDialog(XPropertyAccess_e1d40d20, XExecutableDialog_450f0fa1):
    """
    Service Class

    This service enables a filter developer to register a dialog to query for user options before the filter operation is performed.
    
    The user options are stored inside the com.sun.star.document.MediaDescriptor and can be queried from the com.sun.star.document.MediaDescriptor by the component that implements com.sun.star.document.XFilter.
    
    The application will set the com.sun.star.document.MediaDescriptor using the interface com.sun.star.beans.XPropertyAccess and then call XExecutableDialog.execute().
    
    If that method returns ExecutableDialogResults.OK, the application will retrieve the changed com.sun.star.document.MediaDescriptor back using the interface com.sun.star.beans.XPropertyAccess. The filter operation is then continued, using the new com.sun.star.document.MediaDescriptor.
    
    Otherwise, the filter operation is canceled.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API FilterOptionsDialog <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1FilterOptionsDialog.html>`_
    """
    ...


