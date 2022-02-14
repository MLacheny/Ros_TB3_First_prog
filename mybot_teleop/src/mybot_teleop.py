#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys, termios, tty
import click
from geometry_msgs.msg import Twist

# Arrow keys codes
keys = {'\x1b[A':'up', '\x1b[B':'down', '\x1b[C':'right', '\x1b[D':'left', 's':'stop', 'q':'quit'}

if __name__ == '__main__':
	topic_name = rospy.get_param("/teleop/topic_name")
	pub = rospy.Publisher(topic_name, Twist, queue_size = 1)
	rospy.init_node('mybot_teleop', anonymous=True)
	msg = Twist()
	msg.linear.x = 0
	msg.linear.y = 0
	msg.linear.z = 0
	msg.angular.x = 0
	msg.angular.y = 0
	msg.angular.z = 0
	rate = rospy.Rate(10)
	while(not rospy.is_shutdown()):
		try:
			ang_s = rospy.get_param("/teleop/angular_scale")
			lin_s = rospy.get_param("/teleop/linear_scale")
			topic_name = rospy.get_param("/teleop/topic_name")
			# Get character from console
			mykey = click.getchar()
			if mykey in keys.keys():
				char=keys[mykey]
			if char == 'up':    # UP key
				msg.linear.x = lin_s
				msg.angular.z = 0
			if char == 'down':  # DOWN key
				msg.linear.x = -lin_s
				msg.angular.z = 0
			if char == 'left':  # RIGHT key
				msg.angular.z = ang_s
				msg.linear.x = 0
			if char == 'right': # LEFT
				msg.angular.z = -ang_s
				msg.linear.x = 0
			if char == "quit":  # QUIT
				break
			pub.publish(msg)
			rate.sleep()

		except rospy.ROSInterruptException:
			pass