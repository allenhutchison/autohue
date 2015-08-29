# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='',
  serialized_pb=_b('\n\x0c\x63onfig.proto\" \n\nBridgeInfo\x12\x12\n\nip_address\x18\x01 \x02(\t\"1\n\rAutoHueConfig\x12 \n\x0b\x62ridge_info\x18\x01 \x02(\x0b\x32\x0b.BridgeInfo')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BRIDGEINFO = _descriptor.Descriptor(
  name='BridgeInfo',
  full_name='BridgeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='BridgeInfo.ip_address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=48,
)


_AUTOHUECONFIG = _descriptor.Descriptor(
  name='AutoHueConfig',
  full_name='AutoHueConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bridge_info', full_name='AutoHueConfig.bridge_info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=99,
)

_AUTOHUECONFIG.fields_by_name['bridge_info'].message_type = _BRIDGEINFO
DESCRIPTOR.message_types_by_name['BridgeInfo'] = _BRIDGEINFO
DESCRIPTOR.message_types_by_name['AutoHueConfig'] = _AUTOHUECONFIG

BridgeInfo = _reflection.GeneratedProtocolMessageType('BridgeInfo', (_message.Message,), dict(
  DESCRIPTOR = _BRIDGEINFO,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:BridgeInfo)
  ))
_sym_db.RegisterMessage(BridgeInfo)

AutoHueConfig = _reflection.GeneratedProtocolMessageType('AutoHueConfig', (_message.Message,), dict(
  DESCRIPTOR = _AUTOHUECONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:AutoHueConfig)
  ))
_sym_db.RegisterMessage(AutoHueConfig)


# @@protoc_insertion_point(module_scope)
