#!/usr/bin/python

from __future__ import print_function
import rospy
from std_msgs.msg import Bool,Int8,Float64
import numpy as np
from   rospy.numpy_msg import numpy_msg
from tf.transformations import rotation_matrix 

from geometry_msgs.msg import TransformStamped,Twist

import sys

class obstacle_controller(object):
    def __init__(self):
        self.init_publishers()
        rate=rospy.Rate(10)
        msg=Float64()
        t=20*np.pi
        while not rospy.is_shutdown():
            for i in range(len(self.publishers)):
                if (i%2==0):
                    msg.data=np.sin(t)
                else:
                    msg.data=-np.sin(t)
                self.publishers[i].publish(msg)
            t+=2*np.pi/100
            rate.sleep()

    def init_publishers(self):
        name_ns="/Obs"
        self.publishers=[]
        for i in range(1,5):
            publ=rospy.Publisher(name_ns+str(i)+"/joint_motor_controller/command",Float64,queue_size=10)
            self.publishers.append(publ)