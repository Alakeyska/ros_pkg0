#! /usr/bin/env python3
from study_pkg.msg import Control
import rospy

def callback(msg):
	rospy.loginfo("Wheel status is %s", msg)
	
rospy.init_node('listener_wheels')
rospy.Subscriber('wheel_topic', Control, callback, queue_size=10)
rospy.spin()
