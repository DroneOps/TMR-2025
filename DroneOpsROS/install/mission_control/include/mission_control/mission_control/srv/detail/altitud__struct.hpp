// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mission_control:srv/Altitud.idl
// generated code does not contain a copyright notice

#ifndef MISSION_CONTROL__SRV__DETAIL__ALTITUD__STRUCT_HPP_
#define MISSION_CONTROL__SRV__DETAIL__ALTITUD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__mission_control__srv__Altitud_Request __attribute__((deprecated))
#else
# define DEPRECATED__mission_control__srv__Altitud_Request __declspec(deprecated)
#endif

namespace mission_control
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Altitud_Request_
{
  using Type = Altitud_Request_<ContainerAllocator>;

  explicit Altitud_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->altitud = 0.0;
    }
  }

  explicit Altitud_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->altitud = 0.0;
    }
  }

  // field types and members
  using _altitud_type =
    double;
  _altitud_type altitud;

  // setters for named parameter idiom
  Type & set__altitud(
    const double & _arg)
  {
    this->altitud = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mission_control::srv::Altitud_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const mission_control::srv::Altitud_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mission_control::srv::Altitud_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mission_control::srv::Altitud_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mission_control__srv__Altitud_Request
    std::shared_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mission_control__srv__Altitud_Request
    std::shared_ptr<mission_control::srv::Altitud_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Altitud_Request_ & other) const
  {
    if (this->altitud != other.altitud) {
      return false;
    }
    return true;
  }
  bool operator!=(const Altitud_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Altitud_Request_

// alias to use template instance with default allocator
using Altitud_Request =
  mission_control::srv::Altitud_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace mission_control


#ifndef _WIN32
# define DEPRECATED__mission_control__srv__Altitud_Response __attribute__((deprecated))
#else
# define DEPRECATED__mission_control__srv__Altitud_Response __declspec(deprecated)
#endif

namespace mission_control
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Altitud_Response_
{
  using Type = Altitud_Response_<ContainerAllocator>;

  explicit Altitud_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response_altitud = 0.0;
    }
  }

  explicit Altitud_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->response_altitud = 0.0;
    }
  }

  // field types and members
  using _response_altitud_type =
    double;
  _response_altitud_type response_altitud;

  // setters for named parameter idiom
  Type & set__response_altitud(
    const double & _arg)
  {
    this->response_altitud = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mission_control::srv::Altitud_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const mission_control::srv::Altitud_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mission_control::srv::Altitud_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mission_control::srv::Altitud_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mission_control__srv__Altitud_Response
    std::shared_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mission_control__srv__Altitud_Response
    std::shared_ptr<mission_control::srv::Altitud_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Altitud_Response_ & other) const
  {
    if (this->response_altitud != other.response_altitud) {
      return false;
    }
    return true;
  }
  bool operator!=(const Altitud_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Altitud_Response_

// alias to use template instance with default allocator
using Altitud_Response =
  mission_control::srv::Altitud_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace mission_control

namespace mission_control
{

namespace srv
{

struct Altitud
{
  using Request = mission_control::srv::Altitud_Request;
  using Response = mission_control::srv::Altitud_Response;
};

}  // namespace srv

}  // namespace mission_control

#endif  // MISSION_CONTROL__SRV__DETAIL__ALTITUD__STRUCT_HPP_
