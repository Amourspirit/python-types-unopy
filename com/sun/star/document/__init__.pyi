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
from .._pyi.document.ambigous_filter_request import AmbigousFilterRequest as AmbigousFilterRequest
from .._pyi.document.broken_package_request import BrokenPackageRequest as BrokenPackageRequest
from .._pyi.document.changed_by_others_request import ChangedByOthersRequest as ChangedByOthersRequest
from .._pyi.document.cmis_property import CmisProperty as CmisProperty
from .._pyi.document.cmis_version import CmisVersion as CmisVersion
from .._pyi.document.corrupted_filter_configuration_exception import CorruptedFilterConfigurationException as CorruptedFilterConfigurationException
from .._pyi.document.document_event import DocumentEvent as DocumentEvent
from .._pyi.document.document_properties import DocumentProperties as DocumentProperties
from .._pyi.document.document_revision_list_persistence import DocumentRevisionListPersistence as DocumentRevisionListPersistence
from .._pyi.document.empty_undo_stack_exception import EmptyUndoStackException as EmptyUndoStackException
from .._pyi.document.event_descriptor import EventDescriptor as EventDescriptor
from .._pyi.document.event_object import EventObject as EventObject
from .._pyi.document.events import Events as Events
from .._pyi.document.exotic_file_load_exception import ExoticFileLoadException as ExoticFileLoadException
from .._pyi.document.export_filter import ExportFilter as ExportFilter
from .._pyi.document.extended_type_detection import ExtendedTypeDetection as ExtendedTypeDetection
from .._pyi.document.extended_type_detection_factory import ExtendedTypeDetectionFactory as ExtendedTypeDetectionFactory
from .._pyi.document.filter_adapter import FilterAdapter as FilterAdapter
from .._pyi.document.filter_config_refresh import FilterConfigRefresh as FilterConfigRefresh
from .._pyi.document.filter_factory import FilterFactory as FilterFactory
from .._pyi.document.filter_options_request import FilterOptionsRequest as FilterOptionsRequest
from .._pyi.document.graphic_storage_handler import GraphicStorageHandler as GraphicStorageHandler
from .._pyi.document.header_footer_settings import HeaderFooterSettings as HeaderFooterSettings
from .._pyi.document.import_filter import ImportFilter as ImportFilter
from .._pyi.document.indexed_property_values import IndexedPropertyValues as IndexedPropertyValues
from .._pyi.document.link_target import LinkTarget as LinkTarget
from .._pyi.document.link_targets import LinkTargets as LinkTargets
from .._pyi.document.lock_file_corrupt_request import LockFileCorruptRequest as LockFileCorruptRequest
from .._pyi.document.lock_file_ignore_request import LockFileIgnoreRequest as LockFileIgnoreRequest
from .._pyi.document.locked_document_request import LockedDocumentRequest as LockedDocumentRequest
from .._pyi.document.locked_on_saving_request import LockedOnSavingRequest as LockedOnSavingRequest
from .._pyi.document.media_descriptor import MediaDescriptor as MediaDescriptor
from .._pyi.document.named_property_values import NamedPropertyValues as NamedPropertyValues
from .._pyi.document.no_such_filter_request import NoSuchFilterRequest as NoSuchFilterRequest
from .._pyi.document.ooxml_document_properties_importer import OOXMLDocumentPropertiesImporter as OOXMLDocumentPropertiesImporter
from .._pyi.document.office_document import OfficeDocument as OfficeDocument
from .._pyi.document.ole_embedded_server_registration import OleEmbeddedServerRegistration as OleEmbeddedServerRegistration
from .._pyi.document.own_lock_on_document_request import OwnLockOnDocumentRequest as OwnLockOnDocumentRequest
from .._pyi.document.pdf_dialog import PDFDialog as PDFDialog
from .._pyi.document.reload_editable_request import ReloadEditableRequest as ReloadEditableRequest
from .._pyi.document.settings import Settings as Settings
from .._pyi.document.type_detection import TypeDetection as TypeDetection
from .._pyi.document.undo_context_not_closed_exception import UndoContextNotClosedException as UndoContextNotClosedException
from .._pyi.document.undo_failed_exception import UndoFailedException as UndoFailedException
from .._pyi.document.undo_manager_event import UndoManagerEvent as UndoManagerEvent
from .._pyi.document.x_action_lockable import XActionLockable as XActionLockable
from .._pyi.document.x_binary_stream_resolver import XBinaryStreamResolver as XBinaryStreamResolver
from .._pyi.document.x_cmis_document import XCmisDocument as XCmisDocument
from .._pyi.document.x_code_name_query import XCodeNameQuery as XCodeNameQuery
from .._pyi.document.x_compat_writer_doc_properties import XCompatWriterDocProperties as XCompatWriterDocProperties
from .._pyi.document.x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster
from .._pyi.document.x_document_event_listener import XDocumentEventListener as XDocumentEventListener
from .._pyi.document.x_document_insertable import XDocumentInsertable as XDocumentInsertable
from .._pyi.document.x_document_languages import XDocumentLanguages as XDocumentLanguages
from .._pyi.document.x_document_properties import XDocumentProperties as XDocumentProperties
from .._pyi.document.x_document_properties_supplier import XDocumentPropertiesSupplier as XDocumentPropertiesSupplier
from .._pyi.document.x_document_recovery import XDocumentRecovery as XDocumentRecovery
from .._pyi.document.x_document_revision_list_persistence import XDocumentRevisionListPersistence as XDocumentRevisionListPersistence
from .._pyi.document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier
from .._pyi.document.x_embedded_object_resolver import XEmbeddedObjectResolver as XEmbeddedObjectResolver
from .._pyi.document.x_embedded_object_supplier import XEmbeddedObjectSupplier as XEmbeddedObjectSupplier
from .._pyi.document.x_embedded_object_supplier2 import XEmbeddedObjectSupplier2 as XEmbeddedObjectSupplier2
from .._pyi.document.x_embedded_scripts import XEmbeddedScripts as XEmbeddedScripts
from .._pyi.document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster
from .._pyi.document.x_event_listener import XEventListener as XEventListener
from .._pyi.document.x_events_supplier import XEventsSupplier as XEventsSupplier
from .._pyi.document.x_exporter import XExporter as XExporter
from .._pyi.document.x_extended_filter_detection import XExtendedFilterDetection as XExtendedFilterDetection
from .._pyi.document.x_filter import XFilter as XFilter
from .._pyi.document.x_filter_adapter import XFilterAdapter as XFilterAdapter
from .._pyi.document.x_graphic_object_resolver import XGraphicObjectResolver as XGraphicObjectResolver
from .._pyi.document.x_graphic_storage_handler import XGraphicStorageHandler as XGraphicStorageHandler
from .._pyi.document.x_importer import XImporter as XImporter
from .._pyi.document.x_interaction_filter_options import XInteractionFilterOptions as XInteractionFilterOptions
from .._pyi.document.x_interaction_filter_select import XInteractionFilterSelect as XInteractionFilterSelect
from .._pyi.document.x_link_target_supplier import XLinkTargetSupplier as XLinkTargetSupplier
from .._pyi.document.xml_basic_exporter import XMLBasicExporter as XMLBasicExporter
from .._pyi.document.xml_oasis_basic_exporter import XMLOasisBasicExporter as XMLOasisBasicExporter
from .._pyi.document.x_mime_type_info import XMimeTypeInfo as XMimeTypeInfo
from .._pyi.document.xooxml_document_properties_importer import XOOXMLDocumentPropertiesImporter as XOOXMLDocumentPropertiesImporter
from .._pyi.document.x_redlines_supplier import XRedlinesSupplier as XRedlinesSupplier
from .._pyi.document.x_script_invocation_context import XScriptInvocationContext as XScriptInvocationContext
from .._pyi.document.x_shape_event_broadcaster import XShapeEventBroadcaster as XShapeEventBroadcaster
from .._pyi.document.x_shape_event_listener import XShapeEventListener as XShapeEventListener
from .._pyi.document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument
from .._pyi.document.x_storage_change_listener import XStorageChangeListener as XStorageChangeListener
from .._pyi.document.x_type_detection import XTypeDetection as XTypeDetection
from .._pyi.document.x_undo_action import XUndoAction as XUndoAction
from .._pyi.document.x_undo_manager import XUndoManager as XUndoManager
from .._pyi.document.x_undo_manager_listener import XUndoManagerListener as XUndoManagerListener
from .._pyi.document.x_undo_manager_supplier import XUndoManagerSupplier as XUndoManagerSupplier
from .._pyi.document.x_vba_method_parameter import XVbaMethodParameter as XVbaMethodParameter
from .._pyi.document.x_view_data_supplier import XViewDataSupplier as XViewDataSupplier
from .._pyi.document.xxml_basic_exporter import XXMLBasicExporter as XXMLBasicExporter
