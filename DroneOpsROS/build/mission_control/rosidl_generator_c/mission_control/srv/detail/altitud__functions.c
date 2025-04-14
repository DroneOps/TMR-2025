// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice
#include "mission_control/srv/detail/altitud__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
mission_control__srv__Altitud_Request__init(mission_control__srv__Altitud_Request * msg)
{
  if (!msg) {
    return false;
  }
  // altitud
  return true;
}

void
mission_control__srv__Altitud_Request__fini(mission_control__srv__Altitud_Request * msg)
{
  if (!msg) {
    return;
  }
  // altitud
}

bool
mission_control__srv__Altitud_Request__are_equal(const mission_control__srv__Altitud_Request * lhs, const mission_control__srv__Altitud_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // altitud
  if (lhs->altitud != rhs->altitud) {
    return false;
  }
  return true;
}

bool
mission_control__srv__Altitud_Request__copy(
  const mission_control__srv__Altitud_Request * input,
  mission_control__srv__Altitud_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // altitud
  output->altitud = input->altitud;
  return true;
}

mission_control__srv__Altitud_Request *
mission_control__srv__Altitud_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mission_control__srv__Altitud_Request * msg = (mission_control__srv__Altitud_Request *)allocator.allocate(sizeof(mission_control__srv__Altitud_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mission_control__srv__Altitud_Request));
  bool success = mission_control__srv__Altitud_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mission_control__srv__Altitud_Request__destroy(mission_control__srv__Altitud_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mission_control__srv__Altitud_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mission_control__srv__Altitud_Request__Sequence__init(mission_control__srv__Altitud_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mission_control__srv__Altitud_Request * data = NULL;

  if (size) {
    data = (mission_control__srv__Altitud_Request *)allocator.zero_allocate(size, sizeof(mission_control__srv__Altitud_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mission_control__srv__Altitud_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mission_control__srv__Altitud_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mission_control__srv__Altitud_Request__Sequence__fini(mission_control__srv__Altitud_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mission_control__srv__Altitud_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mission_control__srv__Altitud_Request__Sequence *
mission_control__srv__Altitud_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mission_control__srv__Altitud_Request__Sequence * array = (mission_control__srv__Altitud_Request__Sequence *)allocator.allocate(sizeof(mission_control__srv__Altitud_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mission_control__srv__Altitud_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mission_control__srv__Altitud_Request__Sequence__destroy(mission_control__srv__Altitud_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mission_control__srv__Altitud_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mission_control__srv__Altitud_Request__Sequence__are_equal(const mission_control__srv__Altitud_Request__Sequence * lhs, const mission_control__srv__Altitud_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mission_control__srv__Altitud_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mission_control__srv__Altitud_Request__Sequence__copy(
  const mission_control__srv__Altitud_Request__Sequence * input,
  mission_control__srv__Altitud_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mission_control__srv__Altitud_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mission_control__srv__Altitud_Request * data =
      (mission_control__srv__Altitud_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mission_control__srv__Altitud_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mission_control__srv__Altitud_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mission_control__srv__Altitud_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
mission_control__srv__Altitud_Response__init(mission_control__srv__Altitud_Response * msg)
{
  if (!msg) {
    return false;
  }
  // response_altitud
  return true;
}

void
mission_control__srv__Altitud_Response__fini(mission_control__srv__Altitud_Response * msg)
{
  if (!msg) {
    return;
  }
  // response_altitud
}

bool
mission_control__srv__Altitud_Response__are_equal(const mission_control__srv__Altitud_Response * lhs, const mission_control__srv__Altitud_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // response_altitud
  if (lhs->response_altitud != rhs->response_altitud) {
    return false;
  }
  return true;
}

bool
mission_control__srv__Altitud_Response__copy(
  const mission_control__srv__Altitud_Response * input,
  mission_control__srv__Altitud_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // response_altitud
  output->response_altitud = input->response_altitud;
  return true;
}

mission_control__srv__Altitud_Response *
mission_control__srv__Altitud_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mission_control__srv__Altitud_Response * msg = (mission_control__srv__Altitud_Response *)allocator.allocate(sizeof(mission_control__srv__Altitud_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mission_control__srv__Altitud_Response));
  bool success = mission_control__srv__Altitud_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mission_control__srv__Altitud_Response__destroy(mission_control__srv__Altitud_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mission_control__srv__Altitud_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mission_control__srv__Altitud_Response__Sequence__init(mission_control__srv__Altitud_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mission_control__srv__Altitud_Response * data = NULL;

  if (size) {
    data = (mission_control__srv__Altitud_Response *)allocator.zero_allocate(size, sizeof(mission_control__srv__Altitud_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mission_control__srv__Altitud_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mission_control__srv__Altitud_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mission_control__srv__Altitud_Response__Sequence__fini(mission_control__srv__Altitud_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mission_control__srv__Altitud_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mission_control__srv__Altitud_Response__Sequence *
mission_control__srv__Altitud_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mission_control__srv__Altitud_Response__Sequence * array = (mission_control__srv__Altitud_Response__Sequence *)allocator.allocate(sizeof(mission_control__srv__Altitud_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mission_control__srv__Altitud_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mission_control__srv__Altitud_Response__Sequence__destroy(mission_control__srv__Altitud_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mission_control__srv__Altitud_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mission_control__srv__Altitud_Response__Sequence__are_equal(const mission_control__srv__Altitud_Response__Sequence * lhs, const mission_control__srv__Altitud_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mission_control__srv__Altitud_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mission_control__srv__Altitud_Response__Sequence__copy(
  const mission_control__srv__Altitud_Response__Sequence * input,
  mission_control__srv__Altitud_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mission_control__srv__Altitud_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mission_control__srv__Altitud_Response * data =
      (mission_control__srv__Altitud_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mission_control__srv__Altitud_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mission_control__srv__Altitud_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mission_control__srv__Altitud_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
