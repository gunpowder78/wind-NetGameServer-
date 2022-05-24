# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cPlayer.proto\x12\x0bWindNetwork\"\'\n\x12PlayerLoginRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\"8\n\x13PlayerLoginResponse\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\"7\n\x11\x43reateRoleRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\x05\"H\n\x12\x43reateRoleResponse\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\x05\x12\x0e\n\x06result\x18\x03 \x01(\x08\"G\n\x13SpeakOnWorldRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"G\n\x14SpeakOnWorldResponse\x12\x10\n\x08speak_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\x1f\n\x07Vector2\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"n\n\x11PlayerMoveRequest\x12\"\n\x04move\x18\x01 \x01(\x0b\x32\x14.WindNetwork.Vector2\x12\"\n\x04look\x18\x02 \x01(\x0b\x32\x14.WindNetwork.Vector2\x12\x11\n\tplayer_id\x18\x03 \x01(\t\"o\n\x12PlayerMoveResponse\x12\"\n\x04move\x18\x01 \x01(\x0b\x32\x14.WindNetwork.Vector2\x12\"\n\x04look\x18\x02 \x01(\x0b\x32\x14.WindNetwork.Vector2\x12\x11\n\tplayer_id\x18\x03 \x01(\t\"*\n\x15PlayerJoinRoomRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\";\n\x16PlayerJoinRoomResponse\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x62\x06proto3')



_PLAYERLOGINREQUEST = DESCRIPTOR.message_types_by_name['PlayerLoginRequest']
_PLAYERLOGINRESPONSE = DESCRIPTOR.message_types_by_name['PlayerLoginResponse']
_CREATEROLEREQUEST = DESCRIPTOR.message_types_by_name['CreateRoleRequest']
_CREATEROLERESPONSE = DESCRIPTOR.message_types_by_name['CreateRoleResponse']
_SPEAKONWORLDREQUEST = DESCRIPTOR.message_types_by_name['SpeakOnWorldRequest']
_SPEAKONWORLDRESPONSE = DESCRIPTOR.message_types_by_name['SpeakOnWorldResponse']
_VECTOR3 = DESCRIPTOR.message_types_by_name['Vector3']
_VECTOR2 = DESCRIPTOR.message_types_by_name['Vector2']
_PLAYERMOVEREQUEST = DESCRIPTOR.message_types_by_name['PlayerMoveRequest']
_PLAYERMOVERESPONSE = DESCRIPTOR.message_types_by_name['PlayerMoveResponse']
_PLAYERJOINROOMREQUEST = DESCRIPTOR.message_types_by_name['PlayerJoinRoomRequest']
_PLAYERJOINROOMRESPONSE = DESCRIPTOR.message_types_by_name['PlayerJoinRoomResponse']
PlayerLoginRequest = _reflection.GeneratedProtocolMessageType('PlayerLoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERLOGINREQUEST,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.PlayerLoginRequest)
  })
_sym_db.RegisterMessage(PlayerLoginRequest)

PlayerLoginResponse = _reflection.GeneratedProtocolMessageType('PlayerLoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERLOGINRESPONSE,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.PlayerLoginResponse)
  })
_sym_db.RegisterMessage(PlayerLoginResponse)

CreateRoleRequest = _reflection.GeneratedProtocolMessageType('CreateRoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROLEREQUEST,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.CreateRoleRequest)
  })
_sym_db.RegisterMessage(CreateRoleRequest)

CreateRoleResponse = _reflection.GeneratedProtocolMessageType('CreateRoleResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROLERESPONSE,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.CreateRoleResponse)
  })
_sym_db.RegisterMessage(CreateRoleResponse)

SpeakOnWorldRequest = _reflection.GeneratedProtocolMessageType('SpeakOnWorldRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKONWORLDREQUEST,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.SpeakOnWorldRequest)
  })
_sym_db.RegisterMessage(SpeakOnWorldRequest)

SpeakOnWorldResponse = _reflection.GeneratedProtocolMessageType('SpeakOnWorldResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKONWORLDRESPONSE,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.SpeakOnWorldResponse)
  })
_sym_db.RegisterMessage(SpeakOnWorldResponse)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR3,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.Vector3)
  })
_sym_db.RegisterMessage(Vector3)

Vector2 = _reflection.GeneratedProtocolMessageType('Vector2', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR2,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.Vector2)
  })
_sym_db.RegisterMessage(Vector2)

PlayerMoveRequest = _reflection.GeneratedProtocolMessageType('PlayerMoveRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERMOVEREQUEST,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.PlayerMoveRequest)
  })
_sym_db.RegisterMessage(PlayerMoveRequest)

PlayerMoveResponse = _reflection.GeneratedProtocolMessageType('PlayerMoveResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERMOVERESPONSE,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.PlayerMoveResponse)
  })
_sym_db.RegisterMessage(PlayerMoveResponse)

PlayerJoinRoomRequest = _reflection.GeneratedProtocolMessageType('PlayerJoinRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERJOINROOMREQUEST,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.PlayerJoinRoomRequest)
  })
_sym_db.RegisterMessage(PlayerJoinRoomRequest)

PlayerJoinRoomResponse = _reflection.GeneratedProtocolMessageType('PlayerJoinRoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERJOINROOMRESPONSE,
  '__module__' : 'Player_pb2'
  # @@protoc_insertion_point(class_scope:WindNetwork.PlayerJoinRoomResponse)
  })
_sym_db.RegisterMessage(PlayerJoinRoomResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERLOGINREQUEST._serialized_start=29
  _PLAYERLOGINREQUEST._serialized_end=68
  _PLAYERLOGINRESPONSE._serialized_start=70
  _PLAYERLOGINRESPONSE._serialized_end=126
  _CREATEROLEREQUEST._serialized_start=128
  _CREATEROLEREQUEST._serialized_end=183
  _CREATEROLERESPONSE._serialized_start=185
  _CREATEROLERESPONSE._serialized_end=257
  _SPEAKONWORLDREQUEST._serialized_start=259
  _SPEAKONWORLDREQUEST._serialized_end=330
  _SPEAKONWORLDRESPONSE._serialized_start=332
  _SPEAKONWORLDRESPONSE._serialized_end=403
  _VECTOR3._serialized_start=405
  _VECTOR3._serialized_end=447
  _VECTOR2._serialized_start=449
  _VECTOR2._serialized_end=480
  _PLAYERMOVEREQUEST._serialized_start=482
  _PLAYERMOVEREQUEST._serialized_end=592
  _PLAYERMOVERESPONSE._serialized_start=594
  _PLAYERMOVERESPONSE._serialized_end=705
  _PLAYERJOINROOMREQUEST._serialized_start=707
  _PLAYERJOINROOMREQUEST._serialized_end=749
  _PLAYERJOINROOMRESPONSE._serialized_start=751
  _PLAYERJOINROOMRESPONSE._serialized_end=810
# @@protoc_insertion_point(module_scope)
