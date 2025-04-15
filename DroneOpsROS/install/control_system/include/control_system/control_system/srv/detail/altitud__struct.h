// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from control_system:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__STRUCT_H_
#define CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Altitud in the package control_system.
typedef struct control_system__srv__Altitud_Request
{
  double altitud;
} control_system__srv__Altitud_Request;

// Struct for a sequence of control_system__srv__Altitud_Request.
typedef struct control_system__srv__Altitud_Request__Sequence
{
  control_system__srv__Altitud_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} control_system__srv__Altitud_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Altitud in the package control_system.
typedef struct control_system__srv__Altitud_Response
{
  double response_altitud;
} control_system__srv__Altitud_Response;

// Struct for a sequence of control_system__srv__Altitud_Response.
typedef struct control_system__srv__Altitud_Response__Sequence
{
  control_system__srv__Altitud_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} control_system__srv__Altitud_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__STRUCT_H_
