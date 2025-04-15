// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from control_system:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__BUILDER_HPP_
#define CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "control_system/srv/detail/altitud__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace control_system
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
  ::control_system::srv::Altitud_Request altitud(::control_system::srv::Altitud_Request::_altitud_type arg)
  {
    msg_.altitud = std::move(arg);
    return std::move(msg_);
  }

private:
  ::control_system::srv::Altitud_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::control_system::srv::Altitud_Request>()
{
  return control_system::srv::builder::Init_Altitud_Request_altitud();
}

}  // namespace control_system


namespace control_system
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
  ::control_system::srv::Altitud_Response response_altitud(::control_system::srv::Altitud_Response::_response_altitud_type arg)
  {
    msg_.response_altitud = std::move(arg);
    return std::move(msg_);
  }

private:
  ::control_system::srv::Altitud_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::control_system::srv::Altitud_Response>()
{
  return control_system::srv::builder::Init_Altitud_Response_response_altitud();
}

}  // namespace control_system

#endif  // CONTROL_SYSTEM__SRV__DETAIL__ALTITUD__BUILDER_HPP_
