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
# Namespace: com.sun.star.inspection
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..beans.property import Property as Property_8f4e0a76
    from ..beans.property_state import PropertyState as PropertyState_c97b0c77
    from ..beans.x_property_change_listener import XPropertyChangeListener as XPropertyChangeListener_58e4105a
    from .interactive_selection_result import InteractiveSelectionResult as InteractiveSelectionResult_f27a13e7
    from .line_descriptor import LineDescriptor as LineDescriptor_1e460eeb
    from .x_object_inspector_ui import XObjectInspectorUI as XObjectInspectorUI_5ccd1048
    from .x_property_control_factory import XPropertyControlFactory as XPropertyControlFactory_b8ed12ba
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class XPropertyHandler(XComponent_98dc0ab5):
    """
    is the basic interface for object inspection.
    
    The ObjectInspector itself does not know anything about the object it is inspecting, all information is obtained via XPropertyHandlers. Also, property handlers are responsible for describing the user interface which should be used to interact with the user, with respect to a given aspect of the inspected component.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XPropertyHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XPropertyHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.inspection.XPropertyHandler']

    def actuatingPropertyChanged(self, ActuatingPropertyName: str, NewValue: object, OldValue: object, InspectorUI: 'XObjectInspectorUI_5ccd1048', FirstTimeInit: bool) -> None:
        """
        updates the UI of dependent properties when the value of a certain actuating property changed
        
        This method is called whenever a property value changes, limited to those properties whose changes the handler expressed interest in (see getActuatingProperties()).

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    def addPropertyChangeListener(self, Listener: 'XPropertyChangeListener_58e4105a') -> None:
        """
        registers a listener for notification about property value changes
        
        An XPropertyHandler implementation might decide to ignore this call. However, in this case property value changes made by third party components are not reflected in the object inspector.
        
        If a handler implementation supports property change listeners, it must be able to cope with a call to addPropertyChangeListener() even if currently no component is being inspected. In this case, the listener must become active as soon as a new introspection is set in the next inspect() call.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    def convertToControlValue(self, PropertyName: str, PropertyValue: object, ControlValueType: object) -> object:
        """
        converts a given property value to a control-compatible value
        
        In describePropertyLine(), a property handler declared which type of control should be used to display the value of a certain property. To allow to use the same control type for different properties, and in particular, for properties of different type, conversions between controls values and property values are needed.
        
        This method converts a property value, which has previously been obtained using getPropertyValue(), into a control-compatible value, which can be used with XPropertyControl's XPropertyControl.Value attribute.
        
        A usual application of this method are list boxes: There is a generic list box implementation, which is able to display a simple list of strings. Usually, every string represents one possible property value. To translate between those property values and the displayed strings, convertToControlValue() and convertToPropertyValue() are used.
        
        The method is not invoked if the control's value type (XPropertyControl.ValueType equals the property's value type.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def convertToPropertyValue(self, PropertyName: str, ControlValue: object) -> object:
        """
        converts a given control-compatible value to a property value
        
        In describePropertyLine(), a property handler declared which type of control should be used to display the value of a certain property. To allow to use the same control type for different properties, and in particular, for properties of different type, conversions between controls values and property values are needed.
        
        This method converts a control value into a property value, which subsequently can be used in conjunction with setPropertyValue().

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def describePropertyLine(self, PropertyName: str, ControlFactory: 'XPropertyControlFactory_b8ed12ba') -> 'LineDescriptor_1e460eeb':
        """
        describes the UI to be used to represent the property

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    def getActuatingProperties(self) -> 'typing.Tuple[str, ...]':
        """
        retrieve the actuating properties which this handler is interested in
        
        In general, properties can be declared as \"actuating\", that is, when their value changes, the UI for other properties needs to be updated (e.g. enabled or disabled).
        
        With this method, a handler can declare that it feels responsible for some/all of the depending properties of certain actuating properties.
        
        Whenever the value of an actuating property changes, all handlers which expressed their interest in this particular actuating properties are called with their actuatingPropertyChanged() method.
        
        If getSupportedProperties() returned an empty sequence, this method will not be called
        """
        ...
    def getPropertyState(self, PropertyName: str) -> 'PropertyState_c97b0c77':
        """
        returns the state of a property

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def getPropertyValue(self, PropertyName: str) -> object:
        """
        retrieves the current value of a property

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def getSupersededProperties(self) -> 'typing.Tuple[str, ...]':
        """
        returns the properties which are to be superseded by this handler
        
        Besides defining an own set of properties (see getSupportedProperties()), a property handler can also declare that foreign properties (which it is not responsible for) are superseded by its own properties.
        
        This is usually used if your handler is used with another, more generic one, which should continue to be responsible for all properties, except a few which your handler handles more elegantly.
        
        In such a case, simply return those properties here.
        
        There is a precedence in the property handlers used by an ObjectInspector, which also is important for the superseded properties. This precedence is implied by the precedence of factories to create the property handlers, as denoted in the XObjectInspectorModel.HandlerFactories attribute.
        
        With this in mind, property handlers can only supersede properties which are supported by a handler preceding them, but not properties of handlers succeeding them.
        
        For instance, imaging an XObjectInspectorModel which provides three factories, for handler A, B, and C - in this order. Now if A supports the property Foo, C supports Bar, and B supersedes both Foo and Bar, them the result is Bar is still present. This is because B precedes C, so it cannot, by definition, supersede properties which are supported by C.
        
        If getSupportedProperties() returned an empty sequence, this method will not be called.
        """
        ...
    def getSupportedProperties(self) -> 'typing.Tuple[Property_8f4e0a76, ...]':
        """
        returns the properties which the handler can handle
        
        A handler is allowed to return an empty sequence here, indicating that for the given introspection, no properties handling can be provided. This might happen when a fixed set of property handlers is used for a variety of components to inspect, where not all handlers can really cope with all components.
        
        In the case of returning an empty sequence here, the property handler is ignored by all further processing in the object inspector.
        """
        ...
    def inspect(self, Component: 'XInterface_8f010a43') -> None:
        """
        binds the property handler to a new component

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    def isComposable(self, PropertyName: str) -> bool:
        """
        determines whether a given property, which the handler is responsible for, is composable.
        
        An object inspector can inspect multiple components at once, displaying the intersection of their properties. For this, all components are examined for their properties, and all properties which exist for all components, and are declared to be composable by their respective handler, are displayed in the inspector UI.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def onInteractivePropertySelection(self, PropertyName: str, Primary: bool, outData: object, InspectorUI: 'XObjectInspectorUI_5ccd1048') -> 'InteractiveSelectionResult_f27a13e7':
        """
        called when a browse button belonging to a property UI representation has been clicked
        
        Property handlers can raise a dedicated UI for entering or somehow changing a property value. Usually, this will be a modal dialog, but it can also be a non-modal user interface component.
        
        Availability of this feature is indicated by the LineDescriptor.HasPrimaryButton and LineDescriptor.HasSecondaryButton members of a LineDescriptor, which the XPropertyHandler fills in its describePropertyLine() method.
        
        When this method is called, the property handler should raise the UI needed to enter the property value, and return the result of this (see InteractiveSelectionResult).
        
        It is recommended that property handlers do not directly set the property value which has been obtained from the user, but store it in the output-parameter Data, and return InteractiveSelectionResult.ObtainedValue.
        
        If a handler sets the new property value directly, and returns InteractiveSelectionResult.ObtainedValue, this implies that the property cannot properly be handled in case the object inspector is inspecting an intersection of multiple components, since in this case onInteractivePropertySelection() will be called at one handler only, however the new property would have to be forwarded to all handlers.
        
        If a property is not composable, directly setting the new property value does not yield any problem, as long as property listeners are properly notified of the change.

        * ``outData`` is an out direction argument.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    def removePropertyChangeListener(self, Listener: 'XPropertyChangeListener_58e4105a') -> None:
        """
        revokes a listener for notification about property value changes
        """
        ...
    def setPropertyValue(self, PropertyName: str, Value: object) -> None:
        """
        sets the value of a property

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
        """
        ...
    def suspend(self, Suspend: bool) -> bool:
        """
        suspends the handler
        
        A XPropertyHandler is used by a XObjectInspector instance, which implements the XController interface. By definition, a XObjectInspector always forwards all suspend requests (com.sun.star.frame.XController.suspend()) to all its handlers.
        
        The usual use case for this method are non-modal user interface components used for property value input. Such a component might have been opened during onInteractivePropertySelection(). If a property handler receives a suspend() call, it should forward the suspension request to the UI component, and veto suspension of the XObjectInspector as appropriate.
        
        If suspension is not to be vetoed, then all non-modal UI components opened by the handler should have been closed when it returns from the suspend() call.
        """
        ...


