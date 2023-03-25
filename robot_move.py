#!/usr/bin/env python3
#license removed for brevity

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def move():


    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', String, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1.0

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass


#subscriber for location of the robot - pose

#publisher for movement of the robot - cmd_vel