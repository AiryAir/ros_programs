cmake_minimum_required(VERSION 2.8.3)
project(ros_essentials)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    std_msgs

    message_generation
)

add_service_files(
    FILES
    AddTwoInts.srv
)

## catkin_make to create service