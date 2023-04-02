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
    straightDistance = 10
    straightDistance2 = 10
    speed = 1
    t = 2.54

    goal_rotate = math.pi
    i = 1

    t0 = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():

        while(i==0):
            exit()

        while(i==1):
            while(travelledDistance > 0.0):
                pub.publish(twist)
                t1 = rospy.Time.now().to_sec()
                elapsed = (t1 - t0)
                angularDistance = angularSpeed*elapsed
                linearDistance  = linearSpeed*elapsed
                travelledDistance = travelledDistance - angularDistance
                linearDistance  = linearDistance -angularDistance
                
                rospy.sleep(0.1)
            
            if(travelledDistance < 0.0):
                time.sleep(1)
                t0 = rospy.Time.now().to_sec()
                i=2
                #t0 = rospy.Time.now().to_sec()
        
        while(i==2):
            while(goal_rotate >= t):
                print(goal_rotate)
                twist.linear.x = 0
                # print('goal rotate ', goal_rotate)
                pub.publish(twist)
                t2 = rospy.Time.now().to_sec()
                elapsed2 = t2 - t0
                twist.angular.z = 1
                
                rotate = twist.angular.z * elapsed2
                goal_rotate = goal_rotate - rotate
                # print('rotate ',rotate)
                rospy.sleep(0.1)

                if(goal_rotate <= t):
                    time.sleep(1)           
                    i=3
                    t0 = rospy.Time.now().to_sec()

        while(i==3):
            while(straightDistance >= 0.0):
                sp = twist.linear.x = 1
                twist.angular.z = 0
                pub.publish(twist)
                t3 = rospy.Time.now().to_sec()
                elapsed = t3 - t0
                travelled = sp * elapsed
                straightDistance = straightDistance - travelled
                print(straightDistance, ' - ', travelled)
                # t3 = rospy.Time.now().to_sec()
                # elapsed = t3 - t0
                # distance = twist.linear.x * elapsed
                # straightDistance = straightDistance - distance
                # print(distance)
                if(straightDistance <= 0.0):
                           
                    i=4
                    t0 = rospy.Time.now().to_sec()
                    time.sleep(1)    

        while(i==4):
            while(straightDistance2 >= 0.0):
                sp = twist.linear.x = 1
                twist.angular.z = 0
                pub.publish(twist)
                t4 = rospy.Time.now().to_sec()
                elapsed = t4 - t0
                travelled = sp * elapsed
                straightDistance2 = straightDistance - travelled
                print(straightDistance, ' - ', travelled)
                # t3 = rospy.Time.now().to_sec()
                # elapsed = t3 - t0
                # distance = twist.linear.x * elapsed
                # straightDistance = straightDistance - distance
                # print(distance)
                if(straightDistance2 <= 0.0):
                    exit()



            
if __name__ == '__main__':
    try:
        #Testing our function
        move()
        
    except rospy.ROSInterruptException: pass
