// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef MISSION_CONTROL__SRV__DETAIL__ALTITUD__FUNCTIONS_H_
#define MISSION_CONTROL__SRV__DETAIL__ALTITUD__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "mission_control/msg/rosidl_generator_c__visibility_control.h"

#include "mission_control/srv/detail/altitud__struct.h"

/// Initialize srv/Altitud message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * mission_control__srv__Altitud_Request
 * )) before or use
 * mission_control__srv__Altitud_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Request__init(mission_control__srv__Altitud_Request * msg);

/// Finalize srv/Altitud message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Request__fini(mission_control__srv__Altitud_Request * msg);

/// Create srv/Altitud message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * mission_control__srv__Altitud_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
mission_control__srv__Altitud_Request *
mission_control__srv__Altitud_Request__create();

/// Destroy srv/Altitud message.
/**
 * It calls
 * mission_control__srv__Altitud_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Request__destroy(mission_control__srv__Altitud_Request * msg);

/// Check for srv/Altitud message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Request__are_equal(const mission_control__srv__Altitud_Request * lhs, const mission_control__srv__Altitud_Request * rhs);

/// Copy a srv/Altitud message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Request__copy(
  const mission_control__srv__Altitud_Request * input,
  mission_control__srv__Altitud_Request * output);

/// Initialize array of srv/Altitud messages.
/**
 * It allocates the memory for the number of elements and calls
 * mission_control__srv__Altitud_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Request__Sequence__init(mission_control__srv__Altitud_Request__Sequence * array, size_t size);

/// Finalize array of srv/Altitud messages.
/**
 * It calls
 * mission_control__srv__Altitud_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Request__Sequence__fini(mission_control__srv__Altitud_Request__Sequence * array);

/// Create array of srv/Altitud messages.
/**
 * It allocates the memory for the array and calls
 * mission_control__srv__Altitud_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
mission_control__srv__Altitud_Request__Sequence *
mission_control__srv__Altitud_Request__Sequence__create(size_t size);

/// Destroy array of srv/Altitud messages.
/**
 * It calls
 * mission_control__srv__Altitud_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Request__Sequence__destroy(mission_control__srv__Altitud_Request__Sequence * array);

/// Check for srv/Altitud message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Request__Sequence__are_equal(const mission_control__srv__Altitud_Request__Sequence * lhs, const mission_control__srv__Altitud_Request__Sequence * rhs);

/// Copy an array of srv/Altitud messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Request__Sequence__copy(
  const mission_control__srv__Altitud_Request__Sequence * input,
  mission_control__srv__Altitud_Request__Sequence * output);

/// Initialize srv/Altitud message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * mission_control__srv__Altitud_Response
 * )) before or use
 * mission_control__srv__Altitud_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Response__init(mission_control__srv__Altitud_Response * msg);

/// Finalize srv/Altitud message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Response__fini(mission_control__srv__Altitud_Response * msg);

/// Create srv/Altitud message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * mission_control__srv__Altitud_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
mission_control__srv__Altitud_Response *
mission_control__srv__Altitud_Response__create();

/// Destroy srv/Altitud message.
/**
 * It calls
 * mission_control__srv__Altitud_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Response__destroy(mission_control__srv__Altitud_Response * msg);

/// Check for srv/Altitud message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Response__are_equal(const mission_control__srv__Altitud_Response * lhs, const mission_control__srv__Altitud_Response * rhs);

/// Copy a srv/Altitud message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Response__copy(
  const mission_control__srv__Altitud_Response * input,
  mission_control__srv__Altitud_Response * output);

/// Initialize array of srv/Altitud messages.
/**
 * It allocates the memory for the number of elements and calls
 * mission_control__srv__Altitud_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Response__Sequence__init(mission_control__srv__Altitud_Response__Sequence * array, size_t size);

/// Finalize array of srv/Altitud messages.
/**
 * It calls
 * mission_control__srv__Altitud_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Response__Sequence__fini(mission_control__srv__Altitud_Response__Sequence * array);

/// Create array of srv/Altitud messages.
/**
 * It allocates the memory for the array and calls
 * mission_control__srv__Altitud_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
mission_control__srv__Altitud_Response__Sequence *
mission_control__srv__Altitud_Response__Sequence__create(size_t size);

/// Destroy array of srv/Altitud messages.
/**
 * It calls
 * mission_control__srv__Altitud_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
void
mission_control__srv__Altitud_Response__Sequence__destroy(mission_control__srv__Altitud_Response__Sequence * array);

/// Check for srv/Altitud message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Response__Sequence__are_equal(const mission_control__srv__Altitud_Response__Sequence * lhs, const mission_control__srv__Altitud_Response__Sequence * rhs);

/// Copy an array of srv/Altitud messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mission_control
bool
mission_control__srv__Altitud_Response__Sequence__copy(
  const mission_control__srv__Altitud_Response__Sequence * input,
  mission_control__srv__Altitud_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MISSION_CONTROL__SRV__DETAIL__ALTITUD__FUNCTIONS_H_
