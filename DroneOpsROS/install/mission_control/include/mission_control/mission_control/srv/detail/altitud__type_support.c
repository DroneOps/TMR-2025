// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mission_control/srv/detail/altitud__rosidl_typesupport_introspection_c.h"
#include "mission_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mission_control/srv/detail/altitud__functions.h"
#include "mission_control/srv/detail/altitud__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mission_control__srv__Altitud_Request__init(message_memory);
}

void mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_fini_function(void * message_memory)
{
  mission_control__srv__Altitud_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_member_array[1] = {
  {
    "altitud",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mission_control__srv__Altitud_Request, altitud),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_members = {
  "mission_control__srv",  // message namespace
  "Altitud_Request",  // message name
  1,  // number of fields
  sizeof(mission_control__srv__Altitud_Request),
  mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_member_array,  // message members
  mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_type_support_handle = {
  0,
  &mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mission_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud_Request)() {
  if (!mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_type_support_handle.typesupport_identifier) {
    mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mission_control__srv__Altitud_Request__rosidl_typesupport_introspection_c__Altitud_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "mission_control/srv/detail/altitud__rosidl_typesupport_introspection_c.h"
// already included above
// #include "mission_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "mission_control/srv/detail/altitud__functions.h"
// already included above
// #include "mission_control/srv/detail/altitud__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mission_control__srv__Altitud_Response__init(message_memory);
}

void mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_fini_function(void * message_memory)
{
  mission_control__srv__Altitud_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_member_array[1] = {
  {
    "reponse_altitud",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mission_control__srv__Altitud_Response, reponse_altitud),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_members = {
  "mission_control__srv",  // message namespace
  "Altitud_Response",  // message name
  1,  // number of fields
  sizeof(mission_control__srv__Altitud_Response),
  mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_member_array,  // message members
  mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_type_support_handle = {
  0,
  &mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mission_control
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud_Response)() {
  if (!mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_type_support_handle.typesupport_identifier) {
    mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mission_control__srv__Altitud_Response__rosidl_typesupport_introspection_c__Altitud_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "mission_control/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "mission_control/srv/detail/altitud__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_members = {
  "mission_control__srv",  // service namespace
  "Altitud",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_Request_message_type_support_handle,
  NULL  // response message
  // mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_Response_message_type_support_handle
};

static rosidl_service_type_support_t mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_type_support_handle = {
  0,
  &mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mission_control
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud)() {
  if (!mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_type_support_handle.typesupport_identifier) {
    mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mission_control, srv, Altitud_Response)()->data;
  }

  return &mission_control__srv__detail__altitud__rosidl_typesupport_introspection_c__Altitud_service_type_support_handle;
}
