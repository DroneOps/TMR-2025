// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef MISSION_CONTROL__SRV__DETAIL__ALTITUD__STRUCT_H_
#define MISSION_CONTROL__SRV__DETAIL__ALTITUD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Altitud in the package mission_control.
typedef struct mission_control__srv__Altitud_Request
{
  double altitud;
} mission_control__srv__Altitud_Request;

// Struct for a sequence of mission_control__srv__Altitud_Request.
typedef struct mission_control__srv__Altitud_Request__Sequence
{
  mission_control__srv__Altitud_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mission_control__srv__Altitud_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Altitud in the package mission_control.
typedef struct mission_control__srv__Altitud_Response
{
  double response_altitud;
} mission_control__srv__Altitud_Response;

// Struct for a sequence of mission_control__srv__Altitud_Response.
typedef struct mission_control__srv__Altitud_Response__Sequence
{
  mission_control__srv__Altitud_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mission_control__srv__Altitud_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MISSION_CONTROL__SRV__DETAIL__ALTITUD__STRUCT_H_
