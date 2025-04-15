// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from control_system:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__TRAITS_HPP_
#define CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "control_system/srv/detail/altitud__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace control_system
{

namespace srv
{

inline void to_flow_style_yaml(
  const Altitud_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: altitud
  {
    out << "altitud: ";
    rosidl_generator_traits::value_to_yaml(msg.altitud, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Altitud_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: altitud
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "altitud: ";
    rosidl_generator_traits::value_to_yaml(msg.altitud, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Altitud_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace control_system

namespace rosidl_generator_traits
{

[[deprecated("use control_system::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const control_system::srv::Altitud_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  control_system::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use control_system::srv::to_yaml() instead")]]
inline std::string to_yaml(const control_system::srv::Altitud_Request & msg)
{
  return control_system::srv::to_yaml(msg);
}

template<>
inline const char * data_type<control_system::srv::Altitud_Request>()
{
  return "control_system::srv::Altitud_Request";
}

template<>
inline const char * name<control_system::srv::Altitud_Request>()
{
  return "control_system/srv/Altitud_Request";
}

template<>
struct has_fixed_size<control_system::srv::Altitud_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<control_system::srv::Altitud_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<control_system::srv::Altitud_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace control_system
{

namespace srv
{

inline void to_flow_style_yaml(
  const Altitud_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: response_altitud
  {
    out << "response_altitud: ";
    rosidl_generator_traits::value_to_yaml(msg.response_altitud, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Altitud_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: response_altitud
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "response_altitud: ";
    rosidl_generator_traits::value_to_yaml(msg.response_altitud, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Altitud_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace control_system

namespace rosidl_generator_traits
{

[[deprecated("use control_system::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const control_system::srv::Altitud_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  control_system::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use control_system::srv::to_yaml() instead")]]
inline std::string to_yaml(const control_system::srv::Altitud_Response & msg)
{
  return control_system::srv::to_yaml(msg);
}

template<>
inline const char * data_type<control_system::srv::Altitud_Response>()
{
  return "control_system::srv::Altitud_Response";
}

template<>
inline const char * name<control_system::srv::Altitud_Response>()
{
  return "control_system/srv/Altitud_Response";
}

template<>
struct has_fixed_size<control_system::srv::Altitud_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<control_system::srv::Altitud_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<control_system::srv::Altitud_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<control_system::srv::Altitud>()
{
  return "control_system::srv::Altitud";
}

template<>
inline const char * name<control_system::srv::Altitud>()
{
  return "control_system/srv/Altitud";
}

template<>
struct has_fixed_size<control_system::srv::Altitud>
  : std::integral_constant<
    bool,
    has_fixed_size<control_system::srv::Altitud_Request>::value &&
    has_fixed_size<control_system::srv::Altitud_Response>::value
  >
{
};

template<>
struct has_bounded_size<control_system::srv::Altitud>
  : std::integral_constant<
    bool,
    has_bounded_size<control_system::srv::Altitud_Request>::value &&
    has_bounded_size<control_system::srv::Altitud_Response>::value
  >
{
};

template<>
struct is_service<control_system::srv::Altitud>
  : std::true_type
{
};

template<>
struct is_service_request<control_system::srv::Altitud_Request>
  : std::true_type
{
};

template<>
struct is_service_response<control_system::srv::Altitud_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__TRAITS_HPP_
