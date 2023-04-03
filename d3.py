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


        # while loop for making semi circle
        while(i==1):
            while(travelledDistance > 0.0):                                 # angularDistance is subtracted from travelledDistance
                pub.publish(twist)                                          # velocity is published
                t1 = rospy.Time.now().to_sec()                              # current time (updated every time loop runs)
                elapsed = (t1 - t0)                                         # time elapsed since last loop run
                angularDistance = angularSpeed*elapsed                      # angular distance travelled in that time
                linearDistance  = linearSpeed*elapsed                       # linear distance travelled in that time
                travelledDistance = travelledDistance - angularDistance     # subtract angular distance travelled from travelledDistance
                linearDistance  = linearDistance -angularDistance           # subtract angular distance travelled from linearDistance
                
                rospy.sleep(0.1)                        # sleep for 0.1 seconds
            
            if(travelledDistance < 0.0):                # if travelledDistance is less than 0 run this code
                time.sleep(1)                           # sleep for 1 second
                t0 = rospy.Time.now().to_sec()          # reset t0 to current time
                i=2                                     # set i to 2 to run next loop
        

        # while loop for making rotation of 90 degrees
        while(i==2):
            while(goal_rotate >= t):                    # while goal_rotate is greater than t run this code
                twist.linear.x = 0                      # set linear velocity to 0
                pub.publish(twist)                      # publish velocity
                t2 = rospy.Time.now().to_sec()          # current time (updated every time loop runs)
                elapsed2 = t2 - t0                      # time elapsed since last loop run
                twist.angular.z = 1                     # set angular velocity to 1
                
                rotate = twist.angular.z * elapsed2     # calculate angular distance travelled in that time
                goal_rotate = goal_rotate - rotate      # subtract angular distance travelled from goal_rotate
                rospy.sleep(0.1)                        # sleep for 0.1 seconds

                if(goal_rotate <= t):
                    time.sleep(1)                       # sleep for 1 second
                    i=3                                 # set i to 3 to run next loop
                    t0 = rospy.Time.now().to_sec()      # reset t0 to current time


        # while loop for making straight line (radius: upper circumference to centre)
        while(i==3):
            while(straightDistance >= 0.0):             # while straightDistance is greater than 0 run this code
                sp = twist.linear.x = 1                 # set linear velocity to 1
                twist.angular.z = 0                     # set angular velocity to 0
                pub.publish(twist)                      # publish velocity
                t3 = rospy.Time.now().to_sec()          # current time (updated every time loop runs)
                elapsed = t3 - t0                       # time elapsed since last loop run
                travelled = sp * elapsed                # calculate linear distance travelled in that time
                straightDistance = straightDistance - travelled     # subtract linear distance travelled from straightDistance
                
                if(straightDistance <= 0.0):
                           
                    i=4                                 # set i to 4 to run next loop
                    t0 = rospy.Time.now().to_sec()      # reset t0 to current time
                    time.sleep(1)                       # sleep for 1 second


        # while loop for making straight line (radius: centre to lower circumference)
        while(i==4):
            while(straightDistance2 >= 0.0):            # while straightDistance2 is greater than 0 run this code
                sp = twist.linear.x = 1                 # set linear velocity to 1
                twist.angular.z = 0                     # set angular velocity to 0
                pub.publish(twist)                      # publish velocity
                t4 = rospy.Time.now().to_sec()          # current time (updated every time loop runs)
                elapsed = t4 - t0                       # time elapsed since last loop run
                travelled = sp * elapsed                # calculate linear distance travelled in that time
                straightDistance2 = straightDistance - travelled        # subtract linear distance travelled from straightDistance2
                
                if(straightDistance2 <= 0.0):           
                    exit()                              # exit program



            
if __name__ == '__main__':
    try:
        #Testing our function
        move()
        
    except rospy.ROSInterruptException: pass
