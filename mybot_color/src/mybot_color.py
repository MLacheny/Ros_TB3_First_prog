#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose
from turtlesim.srv import *
import numpy as np


def set_color_client(r):
    rospy.wait_for_service('turtle1/set_pen')
    try:
        set_color = rospy.ServiceProxy('turtle1/set_pen', SetPen)
        set_color(255,r,r,5,0)
    except rospy.ServiceException as e:
        print("Service call failed : %s"%e)

# Callback function for reading turtlesim node output
def read_pose_callback(pos):
    dist = max([abs(5.54 - pos.x),abs(5.54 - pos.y)])
    r_level = 255 - 250*dist/5.54
    set_color_client(int(r_level))


if __name__ == '__main__':
    try:
        rospy.init_node('mybot_color', anonymous=True)
        rospy.Subscriber('turtle1/pose', Pose, read_pose_callback, queue_size = 1)
        # CODE TO BE COMPLETED

        # And then ... wait for the node to be terminated
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
