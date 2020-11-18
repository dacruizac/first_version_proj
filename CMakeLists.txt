cmake_minimum_required(VERSION 3.0.2)
project(first_version_proj)


find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  geometry_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf2_ros
)


catkin_package(

)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)