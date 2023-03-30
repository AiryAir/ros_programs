#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move():
    rospy.init_node('robot_cleaner',anonymous=True)
    twist = Twist()
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    angularSpeed = twist.angular.z = math.pi
    linearSpeed = twist.linear.x = math.pi
    # twist.angular.z = 0
    

    travelledDistance = 1
    straightDistance = 3
    

    t0 = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():
        
        while(travelledDistance > 0.0):
            pub.publish(twist)
            t1 = rospy.Time.now().to_sec()
            elapsed = (t1 - t0)
            angularDistance = angularSpeed*elapsed
            linearDistance  = linearSpeed*elapsed
            travelledDistance = travelledDistance - angularDistance
            linearDistance  = linearDistance -angularDistance

            if(angularDistance <= 0):
                linearSpeed = 0
                angularSpeed = 0
                pub.publish(twist)
                # continue
            rospy.sleep(0.1)



if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
