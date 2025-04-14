// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "mission_control/srv/detail/altitud__struct.h"
#include "mission_control/srv/detail/altitud__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool mission_control__srv__altitud__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[45];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("mission_control.srv._altitud.Altitud_Request", full_classname_dest, 44) == 0);
  }
  mission_control__srv__Altitud_Request * ros_message = _ros_message;
  {  // altitud
    PyObject * field = PyObject_GetAttrString(_pymsg, "altitud");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->altitud = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * mission_control__srv__altitud__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Altitud_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("mission_control.srv._altitud");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Altitud_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  mission_control__srv__Altitud_Request * ros_message = (mission_control__srv__Altitud_Request *)raw_ros_message;
  {  // altitud
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->altitud);
    {
      int rc = PyObject_SetAttrString(_pymessage, "altitud", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "mission_control/srv/detail/altitud__struct.h"
// already included above
// #include "mission_control/srv/detail/altitud__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool mission_control__srv__altitud__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[46];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("mission_control.srv._altitud.Altitud_Response", full_classname_dest, 45) == 0);
  }
  mission_control__srv__Altitud_Response * ros_message = _ros_message;
  {  // response_altitud
    PyObject * field = PyObject_GetAttrString(_pymsg, "response_altitud");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->response_altitud = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * mission_control__srv__altitud__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Altitud_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("mission_control.srv._altitud");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Altitud_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  mission_control__srv__Altitud_Response * ros_message = (mission_control__srv__Altitud_Response *)raw_ros_message;
  {  // response_altitud
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->response_altitud);
    {
      int rc = PyObject_SetAttrString(_pymessage, "response_altitud", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
