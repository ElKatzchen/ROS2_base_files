cmake_minimum_required(VERSION 3.8)
project(Example_C_ws)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(pub src/pub.cpp)
ament_target_dependencies(pub rclcpp std_msgs)

add_executable(pubsub src/pubsub.cpp)
ament_target_dependencies(pubsub rclcpp std_msgs)

add_executable(sub src/sub.cpp)
ament_target_dependencies(sub rclcpp std_msgs)

install(TARGETS
  pub
  pubsub
  sub
  DESTINATION lib/${PROJECT_NAME})

ament_package()