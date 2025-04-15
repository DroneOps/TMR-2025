// generated from rosidl_generator_cpp/resource/rosidl_generator_cpp__visibility_control.hpp.in
// generated code does not contain a copyright notice

#ifndef CONTROL_SYSTEM__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
#define CONTROL_SYSTEM__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_CPP_EXPORT_control_system __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_CPP_IMPORT_control_system __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_CPP_EXPORT_control_system __declspec(dllexport)
    #define ROSIDL_GENERATOR_CPP_IMPORT_control_system __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_CPP_BUILDING_DLL_control_system
    #define ROSIDL_GENERATOR_CPP_PUBLIC_control_system ROSIDL_GENERATOR_CPP_EXPORT_control_system
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_control_system ROSIDL_GENERATOR_CPP_IMPORT_control_system
  #endif
#else
  #define ROSIDL_GENERATOR_CPP_EXPORT_control_system __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_CPP_IMPORT_control_system
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_CPP_PUBLIC_control_system __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_CPP_PUBLIC_control_system
  #endif
#endif

#ifdef __cplusplus
}
#endif

#endif  // CONTROL_SYSTEM__MSG__ROSIDL_GENERATOR_CPP__VISIBILITY_CONTROL_HPP_
