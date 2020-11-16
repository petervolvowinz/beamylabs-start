# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: system_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='system_api.proto',
  package='base',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10system_api.proto\x12\x04\x62\x61se\x1a\x0c\x63ommon.proto\"\x95\x01\n\rConfiguration\x12&\n\x0bnetworkInfo\x18\x01 \x03(\x0b\x32\x11.base.NetworkInfo\x12\x16\n\x0einterfacesJson\x18\x02 \x01(\x0c\x12\x16\n\x0elicenseEndDate\x18\x03 \x01(\t\x12\x15\n\rpublicAddress\x18\x04 \x01(\t\x12\x15\n\rserverVersion\x18\x05 \x01(\t\"_\n\rReloadMessage\x12,\n\rconfiguration\x18\x01 \x01(\x0b\x32\x13.base.ConfigurationH\x00\x12\x16\n\x0c\x65rrorMessage\x18\x02 \x01(\tH\x00\x42\x08\n\x06status\"/\n\x0f\x46ileDescription\x12\x0e\n\x06sha256\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"^\n\x11\x46ileUploadRequest\x12\x30\n\x0f\x66ileDescription\x18\x01 \x01(\x0b\x32\x15.base.FileDescriptionH\x00\x12\x0f\n\x05\x63hunk\x18\x02 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"\xa5\x01\n\x16\x46ileUploadChunkRequest\x12.\n\x0f\x66ileDescription\x18\x01 \x01(\x0b\x32\x15.base.FileDescription\x12\x0e\n\x06\x63hunks\x18\x02 \x01(\r\x12\x0f\n\x07\x63hunkId\x18\x03 \x01(\r\x12\r\n\x05\x63hunk\x18\x04 \x01(\x0c\x12\x14\n\x0c\x63\x61ncelUpload\x18\x05 \x01(\x08\x12\x15\n\ruploadTimeout\x18\x06 \x01(\r\"]\n\x12\x46ileUploadResponse\x12\x12\n\x08\x66inished\x18\x01 \x01(\x08H\x00\x12\x13\n\tcancelled\x18\x02 \x01(\x08H\x00\x12\x16\n\x0c\x65rrorMessage\x18\x03 \x01(\tH\x00\x42\x06\n\x04\x64\x61ta2\xc4\x02\n\rSystemService\x12\x36\n\x10GetConfiguration\x12\x0b.base.Empty\x1a\x13.base.Configuration\"\x00\x12.\n\x0bListSignals\x12\x0f.base.NameSpace\x1a\x0c.base.Frames\"\x00\x12K\n\x0fUploadFileChunk\x12\x1c.base.FileUploadChunkRequest\x1a\x18.base.FileUploadResponse\"\x00\x12\x43\n\nUploadFile\x12\x17.base.FileUploadRequest\x1a\x18.base.FileUploadResponse\"\x00(\x01\x12\x39\n\x13ReloadConfiguration\x12\x0b.base.Empty\x1a\x13.base.ReloadMessage\"\x00\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='base.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkInfo', full_name='base.Configuration.networkInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfacesJson', full_name='base.Configuration.interfacesJson', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='licenseEndDate', full_name='base.Configuration.licenseEndDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicAddress', full_name='base.Configuration.publicAddress', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serverVersion', full_name='base.Configuration.serverVersion', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=190,
)


_RELOADMESSAGE = _descriptor.Descriptor(
  name='ReloadMessage',
  full_name='base.ReloadMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configuration', full_name='base.ReloadMessage.configuration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='base.ReloadMessage.errorMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='status', full_name='base.ReloadMessage.status',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=192,
  serialized_end=287,
)


_FILEDESCRIPTION = _descriptor.Descriptor(
  name='FileDescription',
  full_name='base.FileDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha256', full_name='base.FileDescription.sha256', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='base.FileDescription.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=336,
)


_FILEUPLOADREQUEST = _descriptor.Descriptor(
  name='FileUploadRequest',
  full_name='base.FileUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileDescription', full_name='base.FileUploadRequest.fileDescription', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='base.FileUploadRequest.chunk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='base.FileUploadRequest.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=338,
  serialized_end=432,
)


_FILEUPLOADCHUNKREQUEST = _descriptor.Descriptor(
  name='FileUploadChunkRequest',
  full_name='base.FileUploadChunkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileDescription', full_name='base.FileUploadChunkRequest.fileDescription', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='base.FileUploadChunkRequest.chunks', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunkId', full_name='base.FileUploadChunkRequest.chunkId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='base.FileUploadChunkRequest.chunk', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancelUpload', full_name='base.FileUploadChunkRequest.cancelUpload', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uploadTimeout', full_name='base.FileUploadChunkRequest.uploadTimeout', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=600,
)


_FILEUPLOADRESPONSE = _descriptor.Descriptor(
  name='FileUploadResponse',
  full_name='base.FileUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='finished', full_name='base.FileUploadResponse.finished', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancelled', full_name='base.FileUploadResponse.cancelled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='base.FileUploadResponse.errorMessage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='base.FileUploadResponse.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=602,
  serialized_end=695,
)

_CONFIGURATION.fields_by_name['networkInfo'].message_type = common__pb2._NETWORKINFO
_RELOADMESSAGE.fields_by_name['configuration'].message_type = _CONFIGURATION
_RELOADMESSAGE.oneofs_by_name['status'].fields.append(
  _RELOADMESSAGE.fields_by_name['configuration'])
_RELOADMESSAGE.fields_by_name['configuration'].containing_oneof = _RELOADMESSAGE.oneofs_by_name['status']
_RELOADMESSAGE.oneofs_by_name['status'].fields.append(
  _RELOADMESSAGE.fields_by_name['errorMessage'])
_RELOADMESSAGE.fields_by_name['errorMessage'].containing_oneof = _RELOADMESSAGE.oneofs_by_name['status']
_FILEUPLOADREQUEST.fields_by_name['fileDescription'].message_type = _FILEDESCRIPTION
_FILEUPLOADREQUEST.oneofs_by_name['data'].fields.append(
  _FILEUPLOADREQUEST.fields_by_name['fileDescription'])
_FILEUPLOADREQUEST.fields_by_name['fileDescription'].containing_oneof = _FILEUPLOADREQUEST.oneofs_by_name['data']
_FILEUPLOADREQUEST.oneofs_by_name['data'].fields.append(
  _FILEUPLOADREQUEST.fields_by_name['chunk'])
_FILEUPLOADREQUEST.fields_by_name['chunk'].containing_oneof = _FILEUPLOADREQUEST.oneofs_by_name['data']
_FILEUPLOADCHUNKREQUEST.fields_by_name['fileDescription'].message_type = _FILEDESCRIPTION
_FILEUPLOADRESPONSE.oneofs_by_name['data'].fields.append(
  _FILEUPLOADRESPONSE.fields_by_name['finished'])
_FILEUPLOADRESPONSE.fields_by_name['finished'].containing_oneof = _FILEUPLOADRESPONSE.oneofs_by_name['data']
_FILEUPLOADRESPONSE.oneofs_by_name['data'].fields.append(
  _FILEUPLOADRESPONSE.fields_by_name['cancelled'])
_FILEUPLOADRESPONSE.fields_by_name['cancelled'].containing_oneof = _FILEUPLOADRESPONSE.oneofs_by_name['data']
_FILEUPLOADRESPONSE.oneofs_by_name['data'].fields.append(
  _FILEUPLOADRESPONSE.fields_by_name['errorMessage'])
_FILEUPLOADRESPONSE.fields_by_name['errorMessage'].containing_oneof = _FILEUPLOADRESPONSE.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
DESCRIPTOR.message_types_by_name['ReloadMessage'] = _RELOADMESSAGE
DESCRIPTOR.message_types_by_name['FileDescription'] = _FILEDESCRIPTION
DESCRIPTOR.message_types_by_name['FileUploadRequest'] = _FILEUPLOADREQUEST
DESCRIPTOR.message_types_by_name['FileUploadChunkRequest'] = _FILEUPLOADCHUNKREQUEST
DESCRIPTOR.message_types_by_name['FileUploadResponse'] = _FILEUPLOADRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'system_api_pb2'
  # @@protoc_insertion_point(class_scope:base.Configuration)
  })
_sym_db.RegisterMessage(Configuration)

ReloadMessage = _reflection.GeneratedProtocolMessageType('ReloadMessage', (_message.Message,), {
  'DESCRIPTOR' : _RELOADMESSAGE,
  '__module__' : 'system_api_pb2'
  # @@protoc_insertion_point(class_scope:base.ReloadMessage)
  })
_sym_db.RegisterMessage(ReloadMessage)

FileDescription = _reflection.GeneratedProtocolMessageType('FileDescription', (_message.Message,), {
  'DESCRIPTOR' : _FILEDESCRIPTION,
  '__module__' : 'system_api_pb2'
  # @@protoc_insertion_point(class_scope:base.FileDescription)
  })
_sym_db.RegisterMessage(FileDescription)

FileUploadRequest = _reflection.GeneratedProtocolMessageType('FileUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADREQUEST,
  '__module__' : 'system_api_pb2'
  # @@protoc_insertion_point(class_scope:base.FileUploadRequest)
  })
_sym_db.RegisterMessage(FileUploadRequest)

FileUploadChunkRequest = _reflection.GeneratedProtocolMessageType('FileUploadChunkRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADCHUNKREQUEST,
  '__module__' : 'system_api_pb2'
  # @@protoc_insertion_point(class_scope:base.FileUploadChunkRequest)
  })
_sym_db.RegisterMessage(FileUploadChunkRequest)

FileUploadResponse = _reflection.GeneratedProtocolMessageType('FileUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADRESPONSE,
  '__module__' : 'system_api_pb2'
  # @@protoc_insertion_point(class_scope:base.FileUploadResponse)
  })
_sym_db.RegisterMessage(FileUploadResponse)



_SYSTEMSERVICE = _descriptor.ServiceDescriptor(
  name='SystemService',
  full_name='base.SystemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=698,
  serialized_end=1022,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfiguration',
    full_name='base.SystemService.GetConfiguration',
    index=0,
    containing_service=None,
    input_type=common__pb2._EMPTY,
    output_type=_CONFIGURATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListSignals',
    full_name='base.SystemService.ListSignals',
    index=1,
    containing_service=None,
    input_type=common__pb2._NAMESPACE,
    output_type=common__pb2._FRAMES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadFileChunk',
    full_name='base.SystemService.UploadFileChunk',
    index=2,
    containing_service=None,
    input_type=_FILEUPLOADCHUNKREQUEST,
    output_type=_FILEUPLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='base.SystemService.UploadFile',
    index=3,
    containing_service=None,
    input_type=_FILEUPLOADREQUEST,
    output_type=_FILEUPLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReloadConfiguration',
    full_name='base.SystemService.ReloadConfiguration',
    index=4,
    containing_service=None,
    input_type=common__pb2._EMPTY,
    output_type=_RELOADMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYSTEMSERVICE)

DESCRIPTOR.services_by_name['SystemService'] = _SYSTEMSERVICE

# @@protoc_insertion_point(module_scope)
