// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef MISSION_CONTROL__SRV__DETAIL__ALTITUD__TRAITS_HPP_
#define MISSION_CONTROL__SRV__DETAIL__ALTITUD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "mission_control/srv/detail/altitud__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace mission_control
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

}  // namespace mission_control

namespace rosidl_generator_traits
{

[[deprecated("use mission_control::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mission_control::srv::Altitud_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  mission_control::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mission_control::srv::to_yaml() instead")]]
inline std::string to_yaml(const mission_control::srv::Altitud_Request & msg)
{
  return mission_control::srv::to_yaml(msg);
}

template<>
inline const char * data_type<mission_control::srv::Altitud_Request>()
{
  return "mission_control::srv::Altitud_Request";
}

template<>
inline const char * name<mission_control::srv::Altitud_Request>()
{
  return "mission_control/srv/Altitud_Request";
}

template<>
struct has_fixed_size<mission_control::srv::Altitud_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<mission_control::srv::Altitud_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<mission_control::srv::Altitud_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace mission_control
{

namespace srv
{

inline void to_flow_style_yaml(
  const Altitud_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: reponse_altitud
  {
    out << "reponse_altitud: ";
    rosidl_generator_traits::value_to_yaml(msg.reponse_altitud, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Altitud_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: reponse_altitud
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reponse_altitud: ";
    rosidl_generator_traits::value_to_yaml(msg.reponse_altitud, out);
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

}  // namespace mission_control

namespace rosidl_generator_traits
{

[[deprecated("use mission_control::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mission_control::srv::Altitud_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  mission_control::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mission_control::srv::to_yaml() instead")]]
inline std::string to_yaml(const mission_control::srv::Altitud_Response & msg)
{
  return mission_control::srv::to_yaml(msg);
}

template<>
inline const char * data_type<mission_control::srv::Altitud_Response>()
{
  return "mission_control::srv::Altitud_Response";
}

template<>
inline const char * name<mission_control::srv::Altitud_Response>()
{
  return "mission_control/srv/Altitud_Response";
}

template<>
struct has_fixed_size<mission_control::srv::Altitud_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<mission_control::srv::Altitud_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<mission_control::srv::Altitud_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<mission_control::srv::Altitud>()
{
  return "mission_control::srv::Altitud";
}

template<>
inline const char * name<mission_control::srv::Altitud>()
{
  return "mission_control/srv/Altitud";
}

template<>
struct has_fixed_size<mission_control::srv::Altitud>
  : std::integral_constant<
    bool,
    has_fixed_size<mission_control::srv::Altitud_Request>::value &&
    has_fixed_size<mission_control::srv::Altitud_Response>::value
  >
{
};

template<>
struct has_bounded_size<mission_control::srv::Altitud>
  : std::integral_constant<
    bool,
    has_bounded_size<mission_control::srv::Altitud_Request>::value &&
    has_bounded_size<mission_control::srv::Altitud_Response>::value
  >
{
};

template<>
struct is_service<mission_control::srv::Altitud>
  : std::true_type
{
};

template<>
struct is_service_request<mission_control::srv::Altitud_Request>
  : std::true_type
{
};

template<>
struct is_service_response<mission_control::srv::Altitud_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MISSION_CONTROL__SRV__DETAIL__ALTITUD__TRAITS_HPP_
