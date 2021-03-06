# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_server.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11test_server.proto\x1a\x19google/protobuf/any.proto\":\n\x13ProcessStartedEvent\x12\x12\n\nprocess_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"\x15\n\x13ProcessStoppedEvent\"I\n\x0fNewMessageEvent\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x11\n\trecepient\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"*\n\x14MessageReceivedEvent\x12\x12\n\nmessage_id\x18\x01 \x01(\t\"?\n\x18MessageDataReceivedEvent\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"+\n\x15MessageProcessedEvent\x12\x12\n\nmessage_id\x18\x01 \x01(\t\"A\n\rNewTimerEvent\x12\x10\n\x08timer_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x02\"#\n\x0fTimerFiredEvent\x12\x10\n\x08timer_id\x18\x01 \x01(\t\"\'\n\x13TimerProcessedEvent\x12\x10\n\x08timer_id\x18\x01 \x01(\t\"&\n\x12TimerCanceledEvent\x12\x10\n\x08timer_id\x18\x01 \x01(\t\"-\n\x1aReceiveLocalMessageCommand\x12\x0f\n\x07message\x18\x01 \x01(\x0c\"L\n\x15ReceiveMessageCommand\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"$\n\x10\x46ireTimerCommand\x12\x10\n\x08timer_id\x18\x01 \x01(\t\"\x0e\n\x0c\x43rashCommand2O\n\nTestServer\x12\x41\n\rAttachProcess\x12\x14.google.protobuf.Any\x1a\x14.google.protobuf.Any\"\x00(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_PROCESSSTARTEDEVENT = _descriptor.Descriptor(
  name='ProcessStartedEvent',
  full_name='ProcessStartedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='process_id', full_name='ProcessStartedEvent.process_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='ProcessStartedEvent.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=48,
  serialized_end=106,
)


_PROCESSSTOPPEDEVENT = _descriptor.Descriptor(
  name='ProcessStoppedEvent',
  full_name='ProcessStoppedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=108,
  serialized_end=129,
)


_NEWMESSAGEEVENT = _descriptor.Descriptor(
  name='NewMessageEvent',
  full_name='NewMessageEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='NewMessageEvent.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recepient', full_name='NewMessageEvent.recepient', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='NewMessageEvent.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=131,
  serialized_end=204,
)


_MESSAGERECEIVEDEVENT = _descriptor.Descriptor(
  name='MessageReceivedEvent',
  full_name='MessageReceivedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='MessageReceivedEvent.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=206,
  serialized_end=248,
)


_MESSAGEDATARECEIVEDEVENT = _descriptor.Descriptor(
  name='MessageDataReceivedEvent',
  full_name='MessageDataReceivedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='MessageDataReceivedEvent.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='MessageDataReceivedEvent.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=250,
  serialized_end=313,
)


_MESSAGEPROCESSEDEVENT = _descriptor.Descriptor(
  name='MessageProcessedEvent',
  full_name='MessageProcessedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='MessageProcessedEvent.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=315,
  serialized_end=358,
)


_NEWTIMEREVENT = _descriptor.Descriptor(
  name='NewTimerEvent',
  full_name='NewTimerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer_id', full_name='NewTimerEvent.timer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='NewTimerEvent.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval', full_name='NewTimerEvent.interval', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=360,
  serialized_end=425,
)


_TIMERFIREDEVENT = _descriptor.Descriptor(
  name='TimerFiredEvent',
  full_name='TimerFiredEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer_id', full_name='TimerFiredEvent.timer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=427,
  serialized_end=462,
)


_TIMERPROCESSEDEVENT = _descriptor.Descriptor(
  name='TimerProcessedEvent',
  full_name='TimerProcessedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer_id', full_name='TimerProcessedEvent.timer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=464,
  serialized_end=503,
)


_TIMERCANCELEDEVENT = _descriptor.Descriptor(
  name='TimerCanceledEvent',
  full_name='TimerCanceledEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer_id', full_name='TimerCanceledEvent.timer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=505,
  serialized_end=543,
)


_RECEIVELOCALMESSAGECOMMAND = _descriptor.Descriptor(
  name='ReceiveLocalMessageCommand',
  full_name='ReceiveLocalMessageCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ReceiveLocalMessageCommand.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=545,
  serialized_end=590,
)


_RECEIVEMESSAGECOMMAND = _descriptor.Descriptor(
  name='ReceiveMessageCommand',
  full_name='ReceiveMessageCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='ReceiveMessageCommand.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='ReceiveMessageCommand.sender', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='ReceiveMessageCommand.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=592,
  serialized_end=668,
)


_FIRETIMERCOMMAND = _descriptor.Descriptor(
  name='FireTimerCommand',
  full_name='FireTimerCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer_id', full_name='FireTimerCommand.timer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=670,
  serialized_end=706,
)


_CRASHCOMMAND = _descriptor.Descriptor(
  name='CrashCommand',
  full_name='CrashCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=708,
  serialized_end=722,
)

DESCRIPTOR.message_types_by_name['ProcessStartedEvent'] = _PROCESSSTARTEDEVENT
DESCRIPTOR.message_types_by_name['ProcessStoppedEvent'] = _PROCESSSTOPPEDEVENT
DESCRIPTOR.message_types_by_name['NewMessageEvent'] = _NEWMESSAGEEVENT
DESCRIPTOR.message_types_by_name['MessageReceivedEvent'] = _MESSAGERECEIVEDEVENT
DESCRIPTOR.message_types_by_name['MessageDataReceivedEvent'] = _MESSAGEDATARECEIVEDEVENT
DESCRIPTOR.message_types_by_name['MessageProcessedEvent'] = _MESSAGEPROCESSEDEVENT
DESCRIPTOR.message_types_by_name['NewTimerEvent'] = _NEWTIMEREVENT
DESCRIPTOR.message_types_by_name['TimerFiredEvent'] = _TIMERFIREDEVENT
DESCRIPTOR.message_types_by_name['TimerProcessedEvent'] = _TIMERPROCESSEDEVENT
DESCRIPTOR.message_types_by_name['TimerCanceledEvent'] = _TIMERCANCELEDEVENT
DESCRIPTOR.message_types_by_name['ReceiveLocalMessageCommand'] = _RECEIVELOCALMESSAGECOMMAND
DESCRIPTOR.message_types_by_name['ReceiveMessageCommand'] = _RECEIVEMESSAGECOMMAND
DESCRIPTOR.message_types_by_name['FireTimerCommand'] = _FIRETIMERCOMMAND
DESCRIPTOR.message_types_by_name['CrashCommand'] = _CRASHCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessStartedEvent = _reflection.GeneratedProtocolMessageType('ProcessStartedEvent', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSSTARTEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:ProcessStartedEvent)
  })
_sym_db.RegisterMessage(ProcessStartedEvent)

ProcessStoppedEvent = _reflection.GeneratedProtocolMessageType('ProcessStoppedEvent', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSSTOPPEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:ProcessStoppedEvent)
  })
_sym_db.RegisterMessage(ProcessStoppedEvent)

NewMessageEvent = _reflection.GeneratedProtocolMessageType('NewMessageEvent', (_message.Message,), {
  'DESCRIPTOR' : _NEWMESSAGEEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:NewMessageEvent)
  })
_sym_db.RegisterMessage(NewMessageEvent)

MessageReceivedEvent = _reflection.GeneratedProtocolMessageType('MessageReceivedEvent', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERECEIVEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:MessageReceivedEvent)
  })
_sym_db.RegisterMessage(MessageReceivedEvent)

MessageDataReceivedEvent = _reflection.GeneratedProtocolMessageType('MessageDataReceivedEvent', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDATARECEIVEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:MessageDataReceivedEvent)
  })
_sym_db.RegisterMessage(MessageDataReceivedEvent)

MessageProcessedEvent = _reflection.GeneratedProtocolMessageType('MessageProcessedEvent', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPROCESSEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:MessageProcessedEvent)
  })
_sym_db.RegisterMessage(MessageProcessedEvent)

NewTimerEvent = _reflection.GeneratedProtocolMessageType('NewTimerEvent', (_message.Message,), {
  'DESCRIPTOR' : _NEWTIMEREVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:NewTimerEvent)
  })
_sym_db.RegisterMessage(NewTimerEvent)

TimerFiredEvent = _reflection.GeneratedProtocolMessageType('TimerFiredEvent', (_message.Message,), {
  'DESCRIPTOR' : _TIMERFIREDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:TimerFiredEvent)
  })
_sym_db.RegisterMessage(TimerFiredEvent)

TimerProcessedEvent = _reflection.GeneratedProtocolMessageType('TimerProcessedEvent', (_message.Message,), {
  'DESCRIPTOR' : _TIMERPROCESSEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:TimerProcessedEvent)
  })
_sym_db.RegisterMessage(TimerProcessedEvent)

TimerCanceledEvent = _reflection.GeneratedProtocolMessageType('TimerCanceledEvent', (_message.Message,), {
  'DESCRIPTOR' : _TIMERCANCELEDEVENT,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:TimerCanceledEvent)
  })
_sym_db.RegisterMessage(TimerCanceledEvent)

ReceiveLocalMessageCommand = _reflection.GeneratedProtocolMessageType('ReceiveLocalMessageCommand', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVELOCALMESSAGECOMMAND,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:ReceiveLocalMessageCommand)
  })
_sym_db.RegisterMessage(ReceiveLocalMessageCommand)

ReceiveMessageCommand = _reflection.GeneratedProtocolMessageType('ReceiveMessageCommand', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEMESSAGECOMMAND,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:ReceiveMessageCommand)
  })
_sym_db.RegisterMessage(ReceiveMessageCommand)

FireTimerCommand = _reflection.GeneratedProtocolMessageType('FireTimerCommand', (_message.Message,), {
  'DESCRIPTOR' : _FIRETIMERCOMMAND,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:FireTimerCommand)
  })
_sym_db.RegisterMessage(FireTimerCommand)

CrashCommand = _reflection.GeneratedProtocolMessageType('CrashCommand', (_message.Message,), {
  'DESCRIPTOR' : _CRASHCOMMAND,
  '__module__' : 'test_server_pb2'
  # @@protoc_insertion_point(class_scope:CrashCommand)
  })
_sym_db.RegisterMessage(CrashCommand)



_TESTSERVER = _descriptor.ServiceDescriptor(
  name='TestServer',
  full_name='TestServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=724,
  serialized_end=803,
  methods=[
  _descriptor.MethodDescriptor(
    name='AttachProcess',
    full_name='TestServer.AttachProcess',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_any__pb2._ANY,
    output_type=google_dot_protobuf_dot_any__pb2._ANY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVER)

DESCRIPTOR.services_by_name['TestServer'] = _TESTSERVER

# @@protoc_insertion_point(module_scope)
