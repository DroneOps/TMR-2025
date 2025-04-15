// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from control_system:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__FUNCTIONS_H_
#define CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "control_system/msg/rosidl_generator_c__visibility_control.h"

#include "control_system/srv/detail/altitud__struct.h"

/// Initialize srv/Altitud message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * control_system__srv__Altitud_Request
 * )) before or use
 * control_system__srv__Altitud_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Request__init(control_system__srv__Altitud_Request * msg);

/// Finalize srv/Altitud message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Request__fini(control_system__srv__Altitud_Request * msg);

/// Create srv/Altitud message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * control_system__srv__Altitud_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
control_system__srv__Altitud_Request *
control_system__srv__Altitud_Request__create();

/// Destroy srv/Altitud message.
/**
 * It calls
 * control_system__srv__Altitud_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Request__destroy(control_system__srv__Altitud_Request * msg);

/// Check for srv/Altitud message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Request__are_equal(const control_system__srv__Altitud_Request * lhs, const control_system__srv__Altitud_Request * rhs);

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
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Request__copy(
  const control_system__srv__Altitud_Request * input,
  control_system__srv__Altitud_Request * output);

/// Initialize array of srv/Altitud messages.
/**
 * It allocates the memory for the number of elements and calls
 * control_system__srv__Altitud_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Request__Sequence__init(control_system__srv__Altitud_Request__Sequence * array, size_t size);

/// Finalize array of srv/Altitud messages.
/**
 * It calls
 * control_system__srv__Altitud_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Request__Sequence__fini(control_system__srv__Altitud_Request__Sequence * array);

/// Create array of srv/Altitud messages.
/**
 * It allocates the memory for the array and calls
 * control_system__srv__Altitud_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
control_system__srv__Altitud_Request__Sequence *
control_system__srv__Altitud_Request__Sequence__create(size_t size);

/// Destroy array of srv/Altitud messages.
/**
 * It calls
 * control_system__srv__Altitud_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Request__Sequence__destroy(control_system__srv__Altitud_Request__Sequence * array);

/// Check for srv/Altitud message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Request__Sequence__are_equal(const control_system__srv__Altitud_Request__Sequence * lhs, const control_system__srv__Altitud_Request__Sequence * rhs);

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
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Request__Sequence__copy(
  const control_system__srv__Altitud_Request__Sequence * input,
  control_system__srv__Altitud_Request__Sequence * output);

/// Initialize srv/Altitud message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * control_system__srv__Altitud_Response
 * )) before or use
 * control_system__srv__Altitud_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Response__init(control_system__srv__Altitud_Response * msg);

/// Finalize srv/Altitud message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Response__fini(control_system__srv__Altitud_Response * msg);

/// Create srv/Altitud message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * control_system__srv__Altitud_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
control_system__srv__Altitud_Response *
control_system__srv__Altitud_Response__create();

/// Destroy srv/Altitud message.
/**
 * It calls
 * control_system__srv__Altitud_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Response__destroy(control_system__srv__Altitud_Response * msg);

/// Check for srv/Altitud message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Response__are_equal(const control_system__srv__Altitud_Response * lhs, const control_system__srv__Altitud_Response * rhs);

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
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Response__copy(
  const control_system__srv__Altitud_Response * input,
  control_system__srv__Altitud_Response * output);

/// Initialize array of srv/Altitud messages.
/**
 * It allocates the memory for the number of elements and calls
 * control_system__srv__Altitud_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Response__Sequence__init(control_system__srv__Altitud_Response__Sequence * array, size_t size);

/// Finalize array of srv/Altitud messages.
/**
 * It calls
 * control_system__srv__Altitud_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Response__Sequence__fini(control_system__srv__Altitud_Response__Sequence * array);

/// Create array of srv/Altitud messages.
/**
 * It allocates the memory for the array and calls
 * control_system__srv__Altitud_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
control_system__srv__Altitud_Response__Sequence *
control_system__srv__Altitud_Response__Sequence__create(size_t size);

/// Destroy array of srv/Altitud messages.
/**
 * It calls
 * control_system__srv__Altitud_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
void
control_system__srv__Altitud_Response__Sequence__destroy(control_system__srv__Altitud_Response__Sequence * array);

/// Check for srv/Altitud message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Response__Sequence__are_equal(const control_system__srv__Altitud_Response__Sequence * lhs, const control_system__srv__Altitud_Response__Sequence * rhs);

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
ROSIDL_GENERATOR_C_PUBLIC_control_system
bool
control_system__srv__Altitud_Response__Sequence__copy(
  const control_system__srv__Altitud_Response__Sequence * input,
  control_system__srv__Altitud_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__FUNCTIONS_H_
