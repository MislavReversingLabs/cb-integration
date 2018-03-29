# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cbsdk/cbint.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='cbsdk/cbint.proto',
    package='cbsdk',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x11\x63\x62sdk/cbint.proto\x12\x05\x63\x62sdk\"\x16\n\x06Status\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x0eStatusResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2B\n\nDetonation\x12\x34\n\nget_status\x12\r.cbsdk.Status\x1a\x15.cbsdk.StatusResponse\"\x00\x62\x06proto3')
)

_STATUS = _descriptor.Descriptor(
    name='Status',
    full_name='cbsdk.Status',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='cbsdk.Status.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=28,
    serialized_end=50,
)

_STATUSRESPONSE = _descriptor.Descriptor(
    name='StatusResponse',
    full_name='cbsdk.StatusResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='message', full_name='cbsdk.StatusResponse.message', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=52,
    serialized_end=85,
)

DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
    DESCRIPTOR=_STATUS,
    __module__='cbsdk.cbint_pb2'
    # @@protoc_insertion_point(class_scope:cbsdk.Status)
))
_sym_db.RegisterMessage(Status)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
    DESCRIPTOR=_STATUSRESPONSE,
    __module__='cbsdk.cbint_pb2'
    # @@protoc_insertion_point(class_scope:cbsdk.StatusResponse)
))
_sym_db.RegisterMessage(StatusResponse)

_DETONATION = _descriptor.ServiceDescriptor(
    name='Detonation',
    full_name='cbsdk.Detonation',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=87,
    serialized_end=153,
    methods=[
        _descriptor.MethodDescriptor(
            name='get_status',
            full_name='cbsdk.Detonation.get_status',
            index=0,
            containing_service=None,
            input_type=_STATUS,
            output_type=_STATUSRESPONSE,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_DETONATION)

DESCRIPTOR.services_by_name['Detonation'] = _DETONATION

# @@protoc_insertion_point(module_scope)
