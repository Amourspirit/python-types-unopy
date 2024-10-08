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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form.runtime
from __future__ import annotations
import typing

from ...awt.x_tab_controller import XTabController as XTabController_bacd0be7
from ...container.x_child import XChild as XChild_a6390b07
from ...container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ...container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ..x_confirm_delete_broadcaster import XConfirmDeleteBroadcaster as XConfirmDeleteBroadcaster_6772109f
from ..x_database_parameter_broadcaster2 import XDatabaseParameterBroadcaster2 as XDatabaseParameterBroadcaster2_bee51266
from .x_filter_controller import XFilterController as XFilterController_6b5a10d0
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...sdb.x_row_set_approve_broadcaster import XRowSetApproveBroadcaster as XRowSetApproveBroadcaster_56601044
from ...sdb.xsql_error_broadcaster import XSQLErrorBroadcaster as XSQLErrorBroadcaster_4d10dfd
from ...util.x_mode_selector import XModeSelector as XModeSelector_bbdc0be4
from ...util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
if typing.TYPE_CHECKING:
    from ...awt.x_control import XControl as XControl_7a9c098d
    from ..x_form_controller_listener import XFormControllerListener as XFormControllerListener_49ba1012
    from .x_form_controller_context import XFormControllerContext as XFormControllerContext_c54112e3
    from .x_form_operations import XFormOperations as XFormOperations_4a450ffe
    from ...task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51


class XFormController(XTabController_bacd0be7, XChild_a6390b07, XEnumerationAccess_4bac0ffc, XIndexAccess_f0910d6d, XConfirmDeleteBroadcaster_6772109f, XDatabaseParameterBroadcaster2_bee51266, XFilterController_6b5a10d0, XComponent_98dc0ab5, XRowSetApproveBroadcaster_56601044, XSQLErrorBroadcaster_4d10dfd, XModeSelector_bbdc0be4, XModifyBroadcaster_fd990df0):
    """
    specifies a component controlling the interaction between the user and form functionality.
    
    As soon as a form (containing controls) is to be presented to the user, there is a need for an instance controlling the user interaction.Such a FormController is responsible for dialog processing, like controlling the tab order and the grouping of controls.
    
    As a form may contain one or many subforms, a FormController may contain one or more other FormControllers, so the form model structure or hierarchy is reflected in the structure of FormControllers. That is, retrieving the parent of the model of a controller will give you the same object as retrieving the model of the parent of the controller. Similarly, retrieving the model of the nth child of a controller gives you the same object as retrieving the nth child of the model of the controller.
    
    A controller is called active if one of the controls it is responsible for has the focus, else inactive. To be notified whenever this activation state of a given controller changes, you can add listeners.
    
    This interface supersedes the com.sun.star.form.FormController.
    
    A FormController is responsible for a com.sun.star.awt.UnoControlContainer, and all controls therein.
    
    Furthermore, a form controller is responsible for preventing invalid user input. That is, if the form contains controls bound to a database, or to an external validator, then the form controller will check their current value when the current record is to be saved to the database.
    
    First, it will check whether any controls with an external validator exist. If so, those validators will be asked to validate the current control content. If this fails, the message provided by the validator is displayed to the user, the control is focused, and the update of the record is vetoed.
    
    Second, the controls are examined for NULL values. If a control is bound to a database field which is declared to be NOT NULL, no auto-increment field, but still NULL, then an error message is shown to the user saying that input is required, the respective control is focused, and the update of the record is vetoed.
    
    Note that you can present the second check - for database fields containing NULL values - on a per-form and a per-database basis.For the former, you need to add a boolean property FormsCheckRequiredFields to the form (aka the FormController's model), using its com.sun.star.beans.XPropertyContainer.addProperty() method, with a value of FALSE.For the latter, you need to set the respective property of the data source's Settings (also named FormsCheckRequiredFields) to FALSE.
    
    Alternatively, you can prevent the check on a per-control basis, using the DataAwareControlModel.InputRequired property of a single control model.
    
    If a control which the controller is responsible for supports the com.sun.star.frame.XDispatchProviderInterception interface, the controller registers a dispatch interceptor. Then, the control can try to delegate part of its functionality to the controller by querying the dispatch interceptor for it.
    
    Below, there's a list of URLs which have a defined meaning - if an implementation supports one of them, there must be a guaranteed semantics. However, concrete implementations may support an arbitrary sub or super set of these URLs.
    
    In general, all URLs start with the same prefix, namely .uno:FormController/. To this, a suffix is appended which describes the requested functionality.Example: The URL suffix for deleting the current record is deleteRecord, so the complete URL for requesting a dispatcher for this functionality is .uno:FormController/deleteRecord.
    
    Some URLs may require parameters. For this, the sequence of com.sun.star.beans.PropertyValues passed to the com.sun.star.frame.XDispatch.dispatch() call is used - every property value is used as one named parameter.
    
    For all URLs, interested parties can register as status listeners (com.sun.star.frame.XStatusListener) at the dispatchers, and be notified whenever the functionality associated with the URL becomes enabled or disabled.For instance, the URL with the suffix moveToFirst is associated with moving the form to the first record, and it will be disabled in case the form is already positioned on the first record.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XFormController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1runtime_1_1XFormController.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.form.runtime.XFormController'

    def addActivateListener(self, Listener: XFormControllerListener_49ba1012) -> None:
        """
        adds the specified listener to receive notifications whenever the activation state of the controller changes.
        """
        ...
    def addChildController(self, ChildController: XFormController) -> None:
        """
        adds a controller to the list of child controllers

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def removeActivateListener(self, Listener: XFormControllerListener_49ba1012) -> None:
        """
        removes the specified listener from the list of components to receive notifications whenever the activation state of the controller changes.
        """
        ...

    @property
    def Context(self) -> XFormControllerContext_c54112e3:
        """
        allows to delegate certain tasks to the context of the form controller
        """
        ...
    @Context.setter
    def Context(self, value: XFormControllerContext_c54112e3) -> None:
        ...
    @property
    def CurrentControl(self) -> XControl_7a9c098d:
        """
        provides access to the currently active control
        """
        ...
    @CurrentControl.setter
    def CurrentControl(self, value: XControl_7a9c098d) -> None:
        ...
    @property
    def FormOperations(self) -> XFormOperations_4a450ffe:
        """
        denotes the instance which is used to implement operations on the form which the controller works for.
        
        This instance can be used, for instance, to determine the current state of certain form features.
        """
        ...
    @FormOperations.setter
    def FormOperations(self, value: XFormOperations_4a450ffe) -> None:
        ...
    @property
    def InteractionHandler(self) -> XInteractionHandler_bf80e51:
        """
        used (if not NULL) for user interactions triggered by the form controller.
        """
        ...
    @InteractionHandler.setter
    def InteractionHandler(self, value: XInteractionHandler_bf80e51) -> None:
        ...

