#!/usr/bin/env python
import rospy
import sys
from geometry_msgs.msg import Twist


def move(vel):

    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)



    rospy.init_node('turtlesim', anonymous=True)

    rate = rospy.Rate(1) # 1hz


    while not rospy.is_shutdown():
        twist = Twist()

        twist.linear.x = 1.0
        twist.linear.y = 0
        twist.linear.z = 0

        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = vel

        rate.sleep()

        rospy.loginfo("vel = %f", vel)

        speed_publisher.publish(twist)


if __name__ == '__main__':
    try:
        move(float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass
