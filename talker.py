#!/usr/bin/env python3

from std_msgs import String
#import the String type from std_msgs.msg folder

pub = rospy.Publisher('chatter',String, queue_size=10)
#chatter is the name of the publisher
#String is the type of data - not Python String but std_msgs String
#queue size here will store upto 10 messages for Subscriber backlog

rospy.init_node('talker', anonymous=True)
#initialize a node 'talker'
#anonymous true makes sure all nodes created with the same name have unique IDs

rate = rospy.Rate(1) 						#publishing at 1hz

i=0

while not rospy.is_shutdown():				#while rospy is still running
	hello str = "hello world %s" % i 		#created a string message with a counter
	rospy.loginfo(hello_str) 				#log
	pub.publish(hello_str) 					#publish is the method related to object pub - publishes the message hello_str
	rate.sleep() 							#will sleep for time specified in rospy.Rate, t = 1/f
	i=i+10									#increment the counter
