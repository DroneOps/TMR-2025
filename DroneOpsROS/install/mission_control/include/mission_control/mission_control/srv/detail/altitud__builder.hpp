// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef MISSION_CONTROL__SRV__DETAIL__ALTITUD__BUILDER_HPP_
#define MISSION_CONTROL__SRV__DETAIL__ALTITUD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mission_control/srv/detail/altitud__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mission_control
{

namespace srv
{

namespace builder
{

class Init_Altitud_Request_altitud
{
public:
  Init_Altitud_Request_altitud()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::mission_control::srv::Altitud_Request altitud(::mission_control::srv::Altitud_Request::_altitud_type arg)
  {
    msg_.altitud = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mission_control::srv::Altitud_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mission_control::srv::Altitud_Request>()
{
  return mission_control::srv::builder::Init_Altitud_Request_altitud();
}

}  // namespace mission_control


namespace mission_control
{

namespace srv
{

namespace builder
{

class Init_Altitud_Response_response_altitud
{
public:
  Init_Altitud_Response_response_altitud()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::mission_control::srv::Altitud_Response response_altitud(::mission_control::srv::Altitud_Response::_response_altitud_type arg)
  {
    msg_.response_altitud = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mission_control::srv::Altitud_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mission_control::srv::Altitud_Response>()
{
  return mission_control::srv::builder::Init_Altitud_Response_response_altitud();
}

}  // namespace mission_control

#endif  // MISSION_CONTROL__SRV__DETAIL__ALTITUD__BUILDER_HPP_
