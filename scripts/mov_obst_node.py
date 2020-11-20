#!/usr/bin/python

import rospy
from obst_controller import obstacle_controller

if __name__ == "__main__":
    rospy.init_node("obsctacles_controller",anonymous=True)
    rospy.loginfo("Init node")
    obstacle_controller()
    #rospy.spin()