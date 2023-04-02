#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import time


def move():
    rospy.init_node('robot_cleaner',anonymous=True)
    twist = Twist()
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    angularSpeed = twist.angular.z = math.pi
    linearSpeed = twist.linear.x = math.pi
    # twist.angular.z = 0
    
    travelledDistance = 1
    straightDistance = 3

    goal_rotate = math.pi
    i = 1

    t0 = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():

        while(i==0):
            exit()

        while(i==1):
            print('while 1 loop')            
            while(travelledDistance > 0.0):
                print('travelD loop')
                pub.publish(twist)
                t1 = rospy.Time.now().to_sec()
                elapsed = (t1 - t0)
                angularDistance = angularSpeed*elapsed
                linearDistance  = linearSpeed*elapsed
                travelledDistance = travelledDistance - angularDistance
                linearDistance  = linearDistance -angularDistance
                
                rospy.sleep(0.1)
            
            if(travelledDistance < 0.0):
                print('if thingy')
                time.sleep(3)
                t0 = rospy.Time.now().to_sec()
                i=2
                #t0 = rospy.Time.now().to_sec()
        
        while(i==2):
            print('while 2 loop')
            while(goal_rotate > math.pi/2):
                print('rotate loop')
                # print('goal rotate ', goal_rotate)
                pub.publish(twist)
                t2 = rospy.Time.now().to_sec()
                elapsed2 = t2 - t0
                twist.angular.z = 1
                twist.linear.x = 0
                rotate = twist.angular.z * elapsed2
                goal_rotate = goal_rotate - rotate
                # print('rotate ',rotate)
                rospy.sleep(0.1)

            if(goal_rotate <= 0.0):
                time.sleep(3)
                t0 = rospy.Time.now().to_sec()
                exit()
                

            # while(goal_rotate > 0.0):
            #     pub.publish(twist)
            #     t2 = rospy.Time.now().to_sec()
            #     elapsed = t2 - t0
            #     rotated = (twist.angular.z)*elapsed
            #     goal_rotate = goal_rotate - rotated

            #     if(rotated <= 0):
            #         twist.angular.z = 0
            #         pub.publish(twist)
            #         i = 0

if __name__ == '__main__':
    try:
        #Testing our function
        move()
        
    except rospy.ROSInterruptException: pass
